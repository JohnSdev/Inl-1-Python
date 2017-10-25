


def json_encode( data ):
    if isinstance( data, bool ):
        if data:
            return "true"
        else:
            return "false"
    elif isinstance( data, ( int, float ) ):
        return str( data )
    elif isinstance( data, str ):
        return "NOT IMPLEMENTED, YOU NEED TO IMPLEMENT THIS YOURSELF"
    elif isinstance( data, list ):
        return "NOT IMPLEMENTED, YOU NEED TO IMPLEMENT THIS YOURSELF"
    elif isinstance( data, dict ):
        return "NOT IMPLEMENTED, YOU NEED TO IMPLEMENT THIS YOURSELF"
    else:
        # All other types do not  need to be implemented - it is OK that they raise an error
        raise TypeError( "%s is not JSON serializable" % repr( data ) )

