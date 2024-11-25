from abc import ABC, abstractmethod
import json
from src.port import Port
from src.ship import ShipBuilder, LightWeightShip, MediumShip, HeavyShip
from src.containers import container_factory


def main():
    try:
        with open("input.json") as f:
            data = json.load(f)
    except FileNotFoundError:
        print("Файл 'input.json' не знайдено")
        return
    except json.JSONDecodeError:
        print("Помилка читання JSON-файлу")
        return

    ports = {}
    ships = {}

    for entry in data:
        try:
            if entry["type"] == "port":
                port = Port(entry["id"], entry["latitude"], entry["longitude"])
                ports[port.port_id] = port
                print(f"Порт {port.port_id} створено")

            elif entry["type"] == "ship":
                if entry["port_id"] in ports:
                    port = ports[entry["port_id"]]
                    ship_builder = ShipBuilder().set_ship_type(entry["ship_type"]) \
                        .set_max_weight(entry["max_weight"]) \
                        .set_fuel_capacity(entry["fuel_capacity"])
                    ship = ship_builder.build()
                    ships[ship.name] = ship
                    print(f"Корабель {ship.name} створено та додано до порту {port.port_id}")
                else:
                    print(f"Порт з ID {entry['port_id']} не знайдено для корабля {entry['id']}")

            elif entry["type"] == "container":
                container = container_factory(entry["id"], entry["weight"], entry.get("special"))
                if entry["port_id"] in ports:
                    port = ports[entry["port_id"]]
                    port.load_container(container)
                    print(f"Контейнер {container.id} додано до порту {port.port_id}")
                else:
                    print(f"Порт з ID {entry['port_id']} не знайдено для контейнера {entry['id']}")

        except KeyError as e:
            print(f"Пропущено ключ: {e} в записі: {entry}")
        except Exception as e:
            print(f"Помилка при обробці запису: {entry}. Помилка: {e}")

    for command in data:
        if "action" in command:
            ship = ships.get(command["ship_id"])

            if command["action"] == "load" and ship:
                port = ports.get(command["port_id"])
                container = next((c for c in port.containers if c.id == command["container_id"]), None)
                if container:
                    ship.load_item(container)
                    port.unload_item(container.id)
                    print(f"Контейнер {container.id} завантажено на корабель {ship.name}")

            elif command["action"] == "unload" and ship:
                container = next((c for c in ship.containers if c.id == command["container_id"]), None)
                if container:
                    port = ports.get(command["port_id"])
                    port.load_container(container)
                    ship.unload_item(container)
                    print(f"Контейнер {container.id} розвантажено з корабля {ship.name}")

            elif command["action"] == "sail" and ship:
                destination_port = ports.get(command["destination_port_id"])
                distance = ports[command["port_id"]].calculate_distance(destination_port)
                ship.sail(distance)
                print(f"Корабель {ship.name} вирушив до порту {destination_port.port_id}")

            elif command["action"] == "refuel" and ship:
                ship.refuel(command["amount"])
                print(f"Корабель {ship.name} заправлено на {command['amount']} одиниць")

if __name__ == "__main__":
    main()
