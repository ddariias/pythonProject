import json
from Lab2.src.port import Port
from Lab2.src.ship import Ship
from Lab2.src.conteiners import BasicContainer, RefrigeratedContainer, LiquidContainer, HeavyContainer


def main():
    with open("input.json") as f:
        data = json.load(f)

    ports = {}
    ships = {}

    for entry in data:
        try:
            if entry["type"] == "port":
                port = Port(entry["id"], (entry["latitude"], entry["longitude"]))
                ports[port.id] = port

            elif entry["type"] == "ship":
                if entry["port_id"] in ports:
                    port = ports[entry["port_id"]]
                    container_limits = Ship.ContainerLimits(
                        max_all_containers=entry["max_containers"],
                        max_heavy_containers=entry["max_heavy"],
                        max_refrigerated_containers=entry["max_refrigerated"],
                        max_liquid_containers=entry["max_liquid"]
                    )
                    ship = Ship(
                        id=entry["id"],
                        fuel=entry["fuel"],
                        current_port=port,
                        total_weight_capacity=entry["max_weight"],
                        fuel_consumption_per_km=entry["fuel_consumption_per_km"],
                        container_limits=container_limits
                    )
                    port.incoming_ship(ship)
                    ships[ship.id] = ship
                else:
                    print(f"Port ID {entry['port_id']} not found for Ship {entry['id']}")

            elif entry["type"] == "container":
                if entry["weight"] <= 3000:
                    container = BasicContainer(entry["id"], entry["weight"])
                else:
                    if entry["special"] == "R":
                        container = RefrigeratedContainer(entry["id"], entry["weight"])
                    elif entry["special"] == "L":
                        container = LiquidContainer(entry["id"], entry["weight"])
                    else:
                        container = HeavyContainer(entry["id"], entry["weight"])

                if entry["port_id"] in ports:
                    port = ports[entry["port_id"]]
                    port.containers.append(container)
                else:
                    print(f"Port ID {entry['port_id']} not found for Container {entry['id']}")

        except KeyError as e:
            print(f"Missing key: {e} in entry: {entry}")
        except Exception as e:
            print(f"Error processing entry: {entry}. Error: {e}")

    for command in data:
        if "action" in command:
            ship = ships.get(command["ship_id"])

            if command["action"] == "load" and ship:
                port = ship.current_port
                container = next((c for c in port.containers if c.id == command["container_id"]), None)
                if container and ship.load(container):
                    port.containers.remove(container)
                    print(f"Container {container.id} loaded onto Ship {ship.id}")
                else:
                    print(f"Container {command['container_id']} cannot be loaded onto Ship {ship.id}")

            elif command["action"] == "un_load" and ship:
                container = next((c for c in ship.containers if c.id == command["container_id"]), None)
                if container and ship.un_load(container):
                    print(f"Container {container.id} unloaded from Ship {ship.id}")
                else:
                    print(f"Container {command['container_id']} cannot be unloaded from Ship {ship.id}")

            elif command["action"] == "sail" and ship:
                destination_port = ports.get(command["destination_port_id"])
                if destination_port and ship.sail_to(destination_port):
                    print(f"Ship {ship.id} sailed to Port {destination_port.id}")
                else:
                    print(f"Ship {ship.id} failed to sail to Port {destination_port.id}")

            elif command["action"] == "refuel" and ship:
                ship.re_fuel(command["amount"])
                print(f"Ship {ship.id} refueled by {command['amount']} units. Current fuel: {ship.fuel}")

if __name__ == "__main__":
    main()
