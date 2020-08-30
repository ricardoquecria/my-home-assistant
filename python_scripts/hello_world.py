name = data.get(hass.themes)
logger.info("Hello %s", name)
hass.bus.fire(name, {"wow": "from a Python script!"})


