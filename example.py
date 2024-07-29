from collections import ChainMap
import logging

logging.basicConfig(level=logging.INFO, filename="example.log", filemode="w",
                    format="%(asctime)s %(levelname)s %(""message)s")
logging.debug("A DEBUG Message")
logging.info("An INFO")
logging.warning("A WARNING")
logging.error("An ERROR")
logging.critical("A message of CRITICAL severity")


ex = {
    "AQPartNumber": "Артикул Аквариус",
    "device_family": "семейство устройств",
    "device_type": "базовый класс устройства",
    "components": [
        {
            "type": "базовый класс компоненты",
            "AQPartNumber": "артикул Аквариус компоненты",
            "qty": 1
        }
    ],
    "meta": {
    },
    "attributes": {
        "FRU": {},
        "SMBIOS": {},
        "MACs": {}
    }
}
ch = ChainMap(ex)

if __name__ == "__main__":
    print(ch['attributes']['FRU'])
    print(ch['components'][0]['type'])
