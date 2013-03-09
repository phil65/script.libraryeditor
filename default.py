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
        dialogSelection = xbmcgui.Dialog()
        Edit_Selection = dialogSelection.select( __language__(32007), modeselect ) 
        if Edit_Selection == -1 :
            return
        elif Edit_Selection == 0 :
            self._edit_originaltitle(self._set_string())
        elif Edit_Selection == 1 :
            dialog = xbmcgui.Dialog()
            self._edit_year(dialog.numeric(2013, __language__(32006)))
        elif Edit_Selection == 2 :
            genrestring = self._set_string()
            genrelist = genrestring.split( ' / ' )
            self._edit_genre(json.dumps(genrelist))
        elif Edit_Selection == 3 :
            writerstring = self._set_string()
            writerlist = writerstring.split( ' / ' )
            self._edit_writer(json.dumps(writerstring))
        elif Edit_Selection == 4 :
            directorstring = self._set_string()
            directorlist = directorstring.split( ' / ' )
            self._edit_director(json.dumps(directorlist))
        elif Edit_Selection == 5 :
            self._edit_tagline(self._set_string())
        elif Edit_Selection == 6 :
            self._edit_plot(self._set_string())
        elif Edit_Selection == 7 :
            self._edit_plotoutline(self._set_string()) 
        elif Edit_Selection == 8 :
            dialog = xbmcgui.Dialog()
            self._edit_top250(dialog.numeric(0, __language__(32006))) 
        elif Edit_Selection == 9 :
            self._edit_set(self._set_string())
        elif Edit_Selection == 10 :
            tagstring = self._set_string()
            taglist = tagstring.split( ' / ' )
            self._edit_tag(json.dumps(taglist))
        elif Edit_Selection == 11 :
            countrystring = self._set_string()
            countrylist = countrystring.split( ' / ' )
            self._edit_country(json.dumps(countrylist))
        elif Edit_Selection == 12 :
            studiostring = self._set_string()
            studiolist = studiostring.split( ' / ' )
            self._edit_studio(json.dumps(studiolist))
        elif Edit_Selection == 13 :
            self._edit_mpaa(self._set_string()) 
        elif Edit_Selection == 14 :
            self._edit_trailer(self._set_string()) 
        elif Edit_Selection == 15 :
            showlinkstring = self._set_string()
            showlinklist = showlinkstring.split( ' / ' )
            self._edit_showlink(json.dumps(showlinklist))
        elif Edit_Selection == 16 :
            dialog = xbmcgui.Dialog()
            self._edit_playcount(dialog.numeric(0, __language__(32006)))
            
    def _set_string( self ):
        xbmc.executebuiltin('Skin.Reset(Value)')
        xbmc.executebuiltin('Skin.SetString(Value)')
        time.sleep(1)
        while ((not xbmc.abortRequested) and (xbmc.getCondVisibility('Window.IsActive(virtualkeyboard)'))):
            time.sleep(1)
        return xbmc.getInfoLabel('Skin.String(Value)')
            
    def _edit_title( self,title ):
        xbmc.executeJSONRPC('{"jsonrpc": "2.0", "id": 1, "method": "VideoLibrary.SetMovieDetails", "params": { "title": "%s", "movieid":%s }}' % (title,self.DBID))

    def _edit_originaltitle( self,originaltitle ):
        xbmc.executeJSONRPC('{"jsonrpc": "2.0", "id": 1, "method": "VideoLibrary.SetMovieDetails", "params": { "originaltitle": "%s", "movieid":%s }}' % (originaltitle,self.DBID))
        
    def _edit_genre( self,genre ):
        xbmc.executeJSONRPC('{"jsonrpc": "2.0", "id": 1, "method": "VideoLibrary.SetMovieDetails", "params": { "genre": %s, "movieid":%s }}' % (genre,self.DBID))
        
    def _edit_writer( self,writer ):
        xbmc.executeJSONRPC('{"jsonrpc": "2.0", "id": 1, "method": "VideoLibrary.SetMovieDetails", "params": { "writer": %s, "movieid":%s }}' % (writer,self.DBID))

    def _edit_director( self,director ):
        xbmc.executeJSONRPC('{"jsonrpc": "2.0", "id": 1, "method": "VideoLibrary.SetMovieDetails", "params": { "director": %s, "movieid":%s }}' % (director,self.DBID))
        
    def _edit_studio( self,studio ):
        xbmc.executeJSONRPC('{"jsonrpc": "2.0", "id": 1, "method": "VideoLibrary.SetMovieDetails", "params": { "studio": %s, "movieid":%s }}' % (studio,self.DBID))
 
    def _edit_showlink( self,showlink ):
        xbmc.executeJSONRPC('{"jsonrpc": "2.0", "id": 1, "method": "VideoLibrary.SetMovieDetails", "params": { "showlink": %s, "movieid":%s }}' % (showlink,self.DBID))

    def _edit_tag( self,tag ):
        xbmc.executeJSONRPC('{"jsonrpc": "2.0", "id": 1, "method": "VideoLibrary.SetMovieDetails", "params": { "tag": %s, "movieid":%s }}' % (tag,self.DBID))
        
    def _edit_country( self,country ):
        xbmc.executeJSONRPC('{"jsonrpc": "2.0", "id": 1, "method": "VideoLibrary.SetMovieDetails", "params": { "country": %s, "movieid":%s }}' % (country,self.DBID))
        
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
        
    def _edit_year( self,year ):
        xbmc.executeJSONRPC('{"jsonrpc": "2.0", "id": 1, "method": "VideoLibrary.SetMovieDetails", "params": { "year": %s, "movieid":%s }}' % (year,self.DBID))
        
    def _edit_playcount( self,playcount ):
        xbmc.executeJSONRPC('{"jsonrpc": "2.0", "id": 1, "method": "VideoLibrary.SetMovieDetails", "params": { "playcount": %s, "movieid":%s }}' % (playcount,self.DBID))
        
if ( __name__ == "__main__" ):
    Main()
log('finished')
