import bottle

LOGO = ''' Tournament maker '''

@bottle.get('/')
def zacetna_stran():
    return LOGO

bottle.run()