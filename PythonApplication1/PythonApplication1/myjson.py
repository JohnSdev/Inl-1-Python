


def json_encode( data ):
	if isinstance( data, bool ):
		if data:
			return "true"
		else:
			return "false"
	elif isinstance( data, ( int, float ) ):
		return str( data )
	elif isinstance( data, str ):
		data2 = '"'
		for x in data:
			if x == '\n':
				data2 += '\\n'
			else:
				data2 += x
		data2 += '"'
		return data2
	
	elif isinstance( data, list ):
		data2=('[')
		for x in data:
			data2 += json_encode(x) + ','
		data3 = data2[:-1] + ']'
		return data3
	elif isinstance( data, dict ):
		data2= str(data)
		data3=  data2.replace("'", '"').replace(" ", "").replace("True", "true").replace("False", "false")
		return data3
	else:
		# All other types do not  need to be implemented - it is OK that they raise an error
		raise TypeError( "%s is not JSON serializable" % repr( data ) )

