import sys
import traceback

class Singleton(type):
    ''' Singleton metaclass. Use by defining the metaclass of a class Singleton,
        e.g.: class ThereCanBeOnlyOne:
                  __metaclass__ = Singleton 
    '''              

    def __call__(class_, *args, **kwargs):
	#try:
	if not class_.hasInstance():
	    class_.instance = super(Singleton, class_).__call__(*args, **kwargs)
	return class_.instance
	#except Exception, e:
	#    error_type, error_value, trbk = sys.exc_info()
	#    tb_list = traceback.format_tb(trbk, 6)    
	#    s = "Error: %s \nDescription: %s \nTraceback:" % (error_type.__name__, error_value)
	#    for i in tb_list:
	#	s += "\n" + i

	#    print s
	#    return None

    def deleteInstance(self):
        ''' Delete the (only) instance. This method is mainly for unittests so
            they can start with a clean slate. '''
        if self.hasInstance():
            del self.instance

    def hasInstance(self):
        ''' Has the (only) instance been created already? '''
        return hasattr(self, 'instance')
