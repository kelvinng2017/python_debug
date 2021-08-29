import show_and_save_log_file
import datetime

timeNow = datetime.datetime.now()
file_name_time = timeNow.strftime("%Y-%m-%d_%Hh%Mm%Ss")
file_name_path = "D:/python_debug/log_file/"

log = show_and_save_log_file.Logger(file_name_path+"server "+file_name_time +
                                    ".log", level='debug')
log.logger.debug('jjjj')
show_and_save_log_file.Logger(file_name_path+"server "+file_name_time +
                              ".log", level='debug')
