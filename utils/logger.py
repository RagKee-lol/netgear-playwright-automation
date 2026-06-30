from loguru import logger
logger.add("reports/netgear.log",
	rotation="5MB",
	level="INFO",
	format="{time}|{level}|{message}"
	)
	
