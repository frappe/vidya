# no history

import vidya.api

def get_context(context):
	vidya.api.kernel = None
	k = vidya.api.get_kernel()
	context.no_cache = True
	context.chat = []