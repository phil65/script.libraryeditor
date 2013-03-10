import sys, time
import xbmc, xbmcgui, xbmcaddon
import json

__addon__        = xbmcaddon.Addon()
__addonid__      = __addon__.getAddonInfo('id')
__addonversion__ = __addon__.getAddonInfo('version')
__language__     = __addon__.getLocalizedString

def log(txt):
    if isinstance (txt,str):
        txt = txt.decode("utf-8")
    message = u'%s: %s' % (__addonid__, txt)
    xbmc.log(msg=message.encode("utf-8"), level=xbmc.LOGDEBUG)

class Main:
    def __init__( self ):
        log('version %s started' % __addonversion__ )
        self._parse_argv()
        self._select_dialog()
            
    def _parse_argv( self ):
        try:
            params = dict( arg.split( '=' ) for arg in sys.argv[ 1 ].split( '&' ) )
        except:
            params = {}
        self.DBID = int(params.get( 'DBID', False ))
        
    def _select_dialog( self ):
        if xbmc.getCondVisibility('Container.Content(movies)'):
            self.TYPE = "Movie"
        elif xbmc.getCondVisibility('Container.Content(tvshows)'):
            self.TYPE = "TVShow"
        elif xbmc.getCondVisibility('Container.Content(musicvideos)'):
            self.TYPE = "MusicVideo"
        elif xbmc.getCondVisibility('Container.Content(episodes)'):
            self.TYPE = "Episode"
        modeselect= []  
        modeselect.append( __language__(32008) )
        modeselect.append( __language__(32009) )
        modeselect.append( __language__(32010) )
        modeselect.append( __language__(32011) )
        modeselect.append( __language__(32012) )
        modeselect.append( __language__(32013) )
        modeselect.append( __language__(32014) )
        modeselect.append( __language__(32015) )
        modeselect.append( __language__(32016) )
        modeselect.append( __language__(32017) )
        modeselect.append( __language__(32018) )
        modeselect.append( __language__(32019) )
        modeselect.append( __language__(32020) )
        modeselect.append( __language__(32021) )
        modeselect.append( __language__(32022) )
        modeselect.append( __language__(32023) )
        modeselect.append( __language__(32024) )
        modeselect.append( __language__(32025) )
        dialogSelection = xbmcgui.Dialog()
        Edit_Selection = dialogSelection.select( __language__(32007), modeselect ) 
        if Edit_Selection == -1 :
            return
        elif Edit_Selection == 0 :
            self._edit_originaltitle(self._set_string(xbmc.getInfoLabel('ListItem.OriginalTitle')))
        elif Edit_Selection == 1 :
            dialog = xbmcgui.Dialog()
            self._edit_year(dialog.numeric(2013, __language__(32004)))
        elif Edit_Selection == 2 :
            genrestring = self._set_string(xbmc.getInfoLabel('ListItem.Genre'))
            genrelist = genrestring.split( ' / ' )
            self._edit_label(json.dumps(genrelist),self.TYPE,"genre")
        elif Edit_Selection == 3 :
            writerstring = self._set_string(xbmc.getInfoLabel('ListItem.Writer'))
            writerlist = writerstring.split( ' / ' )
            self._edit_label(json.dumps(writerlist),self.TYPE,"writer")
        elif Edit_Selection == 4 :
            directorstring = self._set_string(xbmc.getInfoLabel('ListItem.Director'))
            directorlist = directorstring.split( ' / ' )
            self._edit_label(json.dumps(directorlist),self.TYPE,"director")
        elif Edit_Selection == 5 :
            self._edit_tagline(self._set_string(xbmc.getInfoLabel('ListItem.Tagline')))
        elif Edit_Selection == 6 :
            self._edit_plot(self._set_string(xbmc.getInfoLabel('ListItem.Plot')))
        elif Edit_Selection == 7 :
            self._edit_plotoutline(self._set_string(xbmc.getInfoLabel('ListItem.PlotOutline'))) 
        elif Edit_Selection == 8 :
            dialog = xbmcgui.Dialog()
            self._edit_top250(dialog.numeric(0, __language__(32006))) 
        elif Edit_Selection == 9 :
            self._edit_set(self._set_string(""))
        elif Edit_Selection == 10 :
            tagstring = self._set_string("")
            taglist = tagstring.split( ' / ' )
            self._edit_label(json.dumps(taglist),self.TYPE,"tag")
        elif Edit_Selection == 11 :
            countrystring = self._set_string(xbmc.getInfoLabel('ListItem.Country'))
            countrylist = countrystring.split( ' / ' )
            self._edit_label(json.dumps(countrylist),self.TYPE,"country")
        elif Edit_Selection == 12 :
            studiostring = self._set_string(xbmc.getInfoLabel('ListItem.Studio'))
            studiolist = studiostring.split( ' / ' )
            self._edit_label(json.dumps(studiolist),self.TYPE,"studio")
        elif Edit_Selection == 13 :
            self._edit_mpaa(self._set_string(xbmc.getInfoLabel('ListItem.Mpaa'))) 
        elif Edit_Selection == 14 :
            self._edit_trailer(self._set_string(xbmc.getInfoLabel('ListItem.Trailer'))) 
        elif Edit_Selection == 15 :
            showlinkstring = self._set_string("")
            showlinklist = showlinkstring.split( ' / ' )
            self._edit_label(json.dumps(showlinklist),self.TYPE,"showlink")
        elif Edit_Selection == 16 :
            dialog = xbmcgui.Dialog()
            self._edit_playcount(dialog.numeric(0, __language__(32005)))
        elif Edit_Selection == 17 :
            self._edit_rating(self._set_string(xbmc.getInfoLabel('ListItem.Rating')))
        self._select_dialog()
            
    def _set_string( self,preset ):
        xbmc.executebuiltin('Skin.Reset(Value)')
        xbmc.executebuiltin('Skin.SetString(Value,%s)' % preset)
        xbmc.executebuiltin('Skin.SetString(Value)')
        while (not xbmc.getCondVisibility('Window.IsActive(virtualkeyboard)')):
            xbmc.sleep(100)
        while ((not xbmc.abortRequested) and (xbmc.getCondVisibility('Window.IsActive(virtualkeyboard)'))):
            xbmc.sleep(100)
        xbmc.sleep(1000)
        return xbmc.getInfoLabel('Skin.String(Value)')
            
    def _edit_title( self,title ):
        xbmc.executeJSONRPC('{"jsonrpc": "2.0", "id": 1, "method": "VideoLibrary.SetMovieDetails", "params": { "title": "%s", "movieid":%s }}' % (title,self.DBID))

    def _edit_originaltitle( self,originaltitle ):
        xbmc.executeJSONRPC('{"jsonrpc": "2.0", "id": 1, "method": "VideoLibrary.SetMovieDetails", "params": { "originaltitle": "%s", "movieid":%s }}' % (originaltitle,self.DBID))
        
    def _edit_label( self,genre,type,label ):
        xbmc.executeJSONRPC('{"jsonrpc": "2.0", "id": 1, "method": "VideoLibrary.Set%sDetails", "params": { "%s": %s, "movieid":%s }}' % (type,label,genre,self.DBID))
                                
    def _edit_mpaa( self,mpaa ):
        xbmc.executeJSONRPC('{"jsonrpc": "2.0", "id": 1, "method": "VideoLibrary.SetMovieDetails", "params": { "mpaa": "%s", "movieid":%s }}' % (mpaa,self.DBID))
        
    def _edit_plot( self,plot ):
        xbmc.executeJSONRPC('{"jsonrpc": "2.0", "id": 1, "method": "VideoLibrary.SetMovieDetails", "params": { "plot": "%s", "movieid":%s }}' % (plot,self.DBID))
        
    def _edit_trailer( self,trailer ):
        xbmc.executeJSONRPC('{"jsonrpc": "2.0", "id": 1, "method": "VideoLibrary.SetMovieDetails", "params": { "trailer": "%s", "movieid":%s }}' % (trailer,self.DBID))
        
    def _edit_tagline( self,tagline ):
        xbmc.executeJSONRPC('{"jsonrpc": "2.0", "id": 1, "method": "VideoLibrary.SetMovieDetails", "params": { "tagline": "%s", "movieid":%s }}' % (tagline,self.DBID))
        
    def _edit_plotoutline( self,plotoutline ):
        xbmc.executeJSONRPC('{"jsonrpc": "2.0", "id": 1, "method": "VideoLibrary.SetMovieDetails", "params": { "plotoutline": "%s", "movieid":%s }}' % (plotoutline,self.DBID))
        
    def _edit_set( self,set ):
        xbmc.executeJSONRPC('{"jsonrpc": "2.0", "id": 1, "method": "VideoLibrary.SetMovieDetails", "params": { "set": "%s", "movieid":%s }}' % (set,self.DBID))
        
    def _edit_top250( self,top250 ):
        xbmc.executeJSONRPC('{"jsonrpc": "2.0", "id": 1, "method": "VideoLibrary.SetMovieDetails", "params": { "top250": %s, "movieid":%s }}' % (top250,self.DBID))

    def _edit_rating( self,rating ):
        xbmc.executeJSONRPC('{"jsonrpc": "2.0", "id": 1, "method": "VideoLibrary.SetMovieDetails", "params": { "rating": %s, "movieid":%s }}' % (rating,self.DBID))
        
    def _edit_year( self,year ):
        xbmc.executeJSONRPC('{"jsonrpc": "2.0", "id": 1, "method": "VideoLibrary.SetMovieDetails", "params": { "year": %s, "movieid":%s }}' % (year,self.DBID))
        
    def _edit_playcount( self,playcount ):
        xbmc.executeJSONRPC('{"jsonrpc": "2.0", "id": 1, "method": "VideoLibrary.SetMovieDetails", "params": { "playcount": %s, "movieid":%s }}' % (playcount,self.DBID))
        
if ( __name__ == "__main__" ):
    Main()
log('finished')
