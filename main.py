import logging
import sys



def my_logging():
	FORMAT = '%(asctime)s %(clientip)-15s %(module_name)-12s %(chicken)-8s %(user)-8s %(message)s'
	logging.basicConfig(format=FORMAT)
	logger = logging.getLogger('tcpserver')
	logger.setLevel(logging.DEBUG)


	d = {
		'module_name': __name__,
		'clientip': '192.168.0.1',
		'user': 'fbloggs',
		'chicken': 'eggs'
	}

	logger.warning('Protocol problem: %s', 'connection reset', extra=d)
	d2 = {
		'module_name': __name__,
		'clientip': '1.2.3.4',
		'user': 'einstein',
		'chicken': 'feathers'
	}
	logger.warning('Some other problem: %s', 'quantum connection reset', extra=d2)

	logger.debug('hello, debug world ', extra=d)


def main():
	my_logging()

if ('__main__'):
	main()
