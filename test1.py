import structlog
logger = structlog.get_logger()
logger.debug("Start uploading file.", file_name=file_name,retries=0)
logger.error("Failed uploading file.", file_name=file_name,retries=retries)
