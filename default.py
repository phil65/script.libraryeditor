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
        self.modeselect= []
        self.identifierlist= []
        if xbmc.getCondVisibility('Container.Content(movies)'):
            self.TYPE = "Movie"
            self._AddToList( xbmc.getLocalizedString(369),"title" )#title
            self._AddToList( xbmc.getLocalizedString(20376),"originaltitle" )#originaltitle
            self._AddToList( xbmc.getLocalizedString(345),"year" )#year
            self._AddToList( xbmc.getLocalizedString(515),"genre" )#genre
            self._AddToList( xbmc.getLocalizedString(20417),"writer" )#writer
            self._AddToList( xbmc.getLocalizedString(20339),"director" )#director
            self._AddToList( xbmc.getLocalizedString(202),"Tagline" )#Tagline
            self._AddToList( xbmc.getLocalizedString(207),"Plot" )#Plot
            self._AddToList( xbmc.getLocalizedString(203),"PlotOutline" )#PlotOutline
            self._AddToList( xbmc.getLocalizedString(13409),"top250" )# top250
            self._AddToList( xbmc.getLocalizedString(20457),"set" )#set
            self._AddToList( xbmc.getLocalizedString(20459),"tag" )#tag
            self._AddToList( xbmc.getLocalizedString(21875),"Country" )#Country
            self._AddToList( xbmc.getLocalizedString(572),"Studio" )#Studio
            self._AddToList( xbmc.getLocalizedString(20074),"MPAA" )#MPAA
            self._AddToList( xbmc.getLocalizedString(20410),"trailer" )#trailer
            self._AddToList( xbmc.getLocalizedString(567),"PlayCount" ) #PlayCount
            self._AddToList( xbmc.getLocalizedString(563),"Rating" ) #Rating
        elif xbmc.getCondVisibility('Container.Content(tvshows)'):
            self.TYPE = "TVShow"
            self._AddToList( xbmc.getLocalizedString(369),"title" )#title
            self._AddToList( xbmc.getLocalizedString(20376),"originaltitle" )#originaltitle
            self._AddToList( xbmc.getLocalizedString(515),"genre" )#genre
            self._AddToList( xbmc.getLocalizedString(207),"Plot" )#Plot
            self._AddToList( xbmc.getLocalizedString(20459),"tag" )#tag
            self._AddToList( xbmc.getLocalizedString(572),"Studio" )#Studio
            self._AddToList( xbmc.getLocalizedString(20074),"MPAA" )#MPAA
            self._AddToList( xbmc.getLocalizedString(567),"PlayCount" )#PlayCount
            self._AddToList( xbmc.getLocalizedString(563),"Rating" )#Rating
            self._AddToList( __language__(32001),"Premiered" )#Premiered
        elif xbmc.getCondVisibility('Container.Content(musicvideos)'):
            self.TYPE = "MusicVideo"
            self._AddToList( xbmc.getLocalizedString(369),"title" )#title
            self._AddToList( xbmc.getLocalizedString(345),"year" )#year
            self._AddToList( xbmc.getLocalizedString(515),"genre" )#genre
            self._AddToList( xbmc.getLocalizedString(20339),"director" )#director
            self._AddToList( xbmc.getLocalizedString(207),"Plot" )#Plot
            self._AddToList( xbmc.getLocalizedString(20459),"tag" )#tag
            self._AddToList( xbmc.getLocalizedString(572),"Studio" )#Studio
            self._AddToList( xbmc.getLocalizedString(567),"PlayCount" )#PlayCount
        #    self._AddToList( xbmc.getLocalizedString(563),"title" )#Rating
            self._AddToList( xbmc.getLocalizedString(558),"Album" )#Album
            self._AddToList( xbmc.getLocalizedString(557),"Artist" )#Artist
            self._AddToList( xbmc.getLocalizedString(554),"Track" )#Track
        elif xbmc.getCondVisibility('Container.Content(episodes)'):
            self.TYPE = "Episode"
            self._AddToList( xbmc.getLocalizedString(369),"title" )#title
            self._AddToList( xbmc.getLocalizedString(20376),"originaltitle" )#originaltitle
            self._AddToList( xbmc.getLocalizedString(515),"genre" )#genre
            self._AddToList( xbmc.getLocalizedString(207),"Plot" )#Plot
            self._AddToList( xbmc.getLocalizedString(20339),"director" )#director
            self._AddToList( xbmc.getLocalizedString(20417),"writer" )#writer
            self._AddToList( xbmc.getLocalizedString(20459),"tag" )#tag
            self._AddToList( xbmc.getLocalizedString(572),"Studio" )#Studio
            self._AddToList( xbmc.getLocalizedString(20074),"MPAA" )#MPAA
            self._AddToList( xbmc.getLocalizedString(567),"PlayCount" )#PlayCount
            self._AddToList( xbmc.getLocalizedString(563),"Rating" )#Rating
            self._AddToList( xbmc.getLocalizedString(20416),"FirstAired" )#FirstAired
    #        self._AddToList( xbmc.getLocalizedString(20416),"title" )#ProductionCode
            self._AddToList( xbmc.getLocalizedString(20373),"Season" )#Season
            self._AddToList( xbmc.getLocalizedString(20359),"Episode" )#Episode
    #        self._AddToList( xbmc.getLocalizedString(20416),"title" )#EpisodeGuide
    #        self._AddToList( xbmc.getLocalizedString(20416),"title" )#imdbnumber
        elif xbmc.getCondVisibility('Container.Content(artists)'):
            self.TYPE = "Artist"
            self._AddToList( xbmc.getLocalizedString(557),"Artist" )#Artist (String)
            self._AddToList( xbmc.getLocalizedString(515),"genre" )#genre
            self._AddToList( xbmc.getLocalizedString(21893),"born" )#born
            self._AddToList( xbmc.getLocalizedString(21894),"formed" )#formed
            self._AddToList( xbmc.getLocalizedString(21821),"description" )#description
            self._AddToList( xbmc.getLocalizedString(21897),"died" )#died
            self._AddToList( xbmc.getLocalizedString(21896),"disbanded" )#disbanded
            self._AddToList( xbmc.getLocalizedString(21898),"yearsactive" )#yearsactive
            self._AddToList( xbmc.getLocalizedString(175),"Mood" )#Mood
            self._AddToList( xbmc.getLocalizedString(176),"Style" )#Style
            self._AddToList( xbmc.getLocalizedString(21892),"Instrument" )#Instrument
        elif xbmc.getCondVisibility('Container.Content(albums)'):
            self.TYPE = "Album"
            self._AddToList( xbmc.getLocalizedString(369),"title" )#title
            self._AddToList( xbmc.getLocalizedString(557),"Artist" )#Artist (Array)
            self._AddToList( xbmc.getLocalizedString(345),"year" )#year
            self._AddToList( xbmc.getLocalizedString(175),"Mood" )#Mood
            self._AddToList( xbmc.getLocalizedString(176),"Style" )#Style
            self._AddToList( xbmc.getLocalizedString(515),"genre" )#genre
            self._AddToList( xbmc.getLocalizedString(21895),"themes" )#themes
         #   self._AddToList( xbmc.getLocalizedString(515),"type" )#type
          #  self._AddToList( xbmc.getLocalizedString(515),"albumlabel" )#albumlabel
            self._AddToList( xbmc.getLocalizedString(21821),"description" )#description
            self._AddToList( xbmc.getLocalizedString(563),"Rating" )#Rating
        elif xbmc.getCondVisibility('Container.Content(songs)'):
            self.TYPE = "Song"
            self._AddToList( xbmc.getLocalizedString(369),"title" )#title
            self._AddToList( xbmc.getLocalizedString(557),"Artist" )#Artist (Array)
            self._AddToList( xbmc.getLocalizedString(557),"AlbumArtist" )#AlbumArtist (Array)
            self._AddToList( xbmc.getLocalizedString(557),"Album" )#Album
            self._AddToList( xbmc.getLocalizedString(515),"genre" )#genre
            self._AddToList( xbmc.getLocalizedString(345),"year" )#year
            self._AddToList( xbmc.getLocalizedString(563),"Rating" )#Rating
            self._AddToList( xbmc.getLocalizedString(569),"Comment" )#Comment
            self._AddToList( xbmc.getLocalizedString(427),"Disc" )#Disc
            self._AddToList( xbmc.getLocalizedString(554),"Track" )#Track
          
        dialogSelection = xbmcgui.Dialog()
        Edit_Selection = dialogSelection.select( __language__(32007), self.modeselect ) 
        if Edit_Selection == -1 :
            return
        elif self.modeselect[Edit_Selection] == xbmc.getLocalizedString(369) :         #Title
            self._edit_db_tag(json.dumps(self._set_string(xbmc.getInfoLabel('ListItem.Title'))),self.TYPE,"title")
        elif self.modeselect[Edit_Selection] == xbmc.getLocalizedString(20376) :         #OriginalTitle
            self._edit_db_tag(json.dumps(self._set_string(xbmc.getInfoLabel('ListItem.OriginalTitle'))),self.TYPE,"originaltitle")
        elif self.modeselect[Edit_Selection] == xbmc.getLocalizedString(345) :         #Year
            self._edit_db_tag(xbmcgui.Dialog().numeric(0, xbmc.getLocalizedString(16028)),self.TYPE,"year")
        elif self.modeselect[Edit_Selection] == xbmc.getLocalizedString(20359) :         #Episode
            self._edit_db_tag(xbmcgui.Dialog().numeric(0, xbmc.getLocalizedString(16028)),self.TYPE,"episode")
        elif self.modeselect[Edit_Selection] == xbmc.getLocalizedString(20373) :         #Season
            self._edit_db_tag(xbmcgui.Dialog().numeric(0, xbmc.getLocalizedString(16028)),self.TYPE,"season")
        elif self.modeselect[Edit_Selection] == xbmc.getLocalizedString(554) :         #track
            self._edit_db_tag(xbmcgui.Dialog().numeric(0, xbmc.getLocalizedString(16028)),self.TYPE,"track")
        elif self.modeselect[Edit_Selection] == xbmc.getLocalizedString(427) :         #disc
            self._edit_db_tag(xbmcgui.Dialog().numeric(0, xbmc.getLocalizedString(16028)),self.TYPE,"disc")
        elif self.modeselect[Edit_Selection] == xbmc.getLocalizedString(515) :         #Genre
            genrestring = self._set_string(xbmc.getInfoLabel('ListItem.Genre'))
            self._edit_db_tag(json.dumps(genrestring.split( ' / ' )),self.TYPE,"genre")
        elif self.modeselect[Edit_Selection] == xbmc.getLocalizedString(20417) :         #Writer
            writerstring = self._set_string(xbmc.getInfoLabel('ListItem.Writer'))
            self._edit_db_tag(json.dumps(writerstring.split( ' / ' )),self.TYPE,"writer")
        elif self.modeselect[Edit_Selection] == xbmc.getLocalizedString(20339) :         #Director
            directorstring = self._set_string(xbmc.getInfoLabel('ListItem.Director'))
            self._edit_db_tag(json.dumps(directorstring.split( ' / ' )),self.TYPE,"director")
        elif self.modeselect[Edit_Selection] == xbmc.getLocalizedString(202) :         #Tagline
            self._edit_db_tag(json.dumps(self._set_string(xbmc.getInfoLabel('ListItem.Tagline'))),self.TYPE,"tagline")
        elif self.modeselect[Edit_Selection] == xbmc.getLocalizedString(207) :         #Plot
            self._edit_db_tag(json.dumps(self._set_string(xbmc.getInfoLabel('ListItem.Plot'))),self.TYPE,"plot")
        elif self.modeselect[Edit_Selection] == xbmc.getLocalizedString(203) :         #PlotOutlne
            self._edit_db_tag(json.dumps(self._set_string(xbmc.getInfoLabel('ListItem.PlotOutline'))),self.TYPE,"plotoutline")
        elif self.modeselect[Edit_Selection] == xbmc.getLocalizedString(13409) :         #Top250
            self._edit_db_tag(xbmcgui.Dialog().numeric(0, xbmc.getLocalizedString(16028)),self.TYPE,"top250")
        elif self.modeselect[Edit_Selection] == xbmc.getLocalizedString(20457) :         #Set
            self._edit_db_tag(json.dumps(self._set_string("")),self.TYPE,"set")
        elif self.modeselect[Edit_Selection] == xbmc.getLocalizedString(20459) :         #Tag
            tagstring = self._set_string("") 
            self._edit_db_tag(json.dumps(tagstring.split( ' / ' )),self.TYPE,"tag")
        elif self.modeselect[Edit_Selection] == xbmc.getLocalizedString(21875) :         #Country
            countrystring = self._set_string(xbmc.getInfoLabel('ListItem.Country'))
            self._edit_db_tag(json.dumps(countrystring.split( ' / ' )),self.TYPE,"country")
        elif self.modeselect[Edit_Selection] == xbmc.getLocalizedString(572) :         #Studio
            studiostring = self._set_string(xbmc.getInfoLabel('ListItem.Studio'))
            self._edit_db_tag(json.dumps(studiostring.split( ' / ' )),self.TYPE,"studio")
        elif self.modeselect[Edit_Selection] == xbmc.getLocalizedString(20074) :         #Mpaa
            self._edit_db_tag(json.dumps(self._set_string(xbmc.getInfoLabel('ListItem.Mpaa'))),self.TYPE,"mpaa")
        elif self.modeselect[Edit_Selection] == xbmc.getLocalizedString(20410) :         #Trailer
            self._edit_db_tag(json.dumps(self._set_string(xbmc.getInfoLabel('ListItem.Trailer'))),self.TYPE,"trailer")
        elif self.modeselect[Edit_Selection] == xbmc.getLocalizedString(567) :            #PlayCount
            self._edit_db_tag(xbmcgui.Dialog().numeric(0, xbmc.getLocalizedString(16028)),self.TYPE,"playcount")
        elif self.modeselect[Edit_Selection] == xbmc.getLocalizedString(563) :            #Rating
            self._edit_db_tag(self._set_string(xbmc.getInfoLabel('ListItem.Rating')),self.TYPE,"rating")
        elif self.modeselect[Edit_Selection] == __language__(32001) :             #Premiered
            self._edit_db_tag(json.dumps(self._set_string(xbmc.getInfoLabel('ListItem.Premiered'))),self.TYPE,"premiered")
        elif self.modeselect[Edit_Selection] == xbmc.getLocalizedString(557) :             #Artist
            artiststring = self._set_string("")
            self._edit_db_tag(json.dumps(artiststring.split( ' / ' )),self.TYPE,"artist")
        elif self.modeselect[Edit_Selection] == xbmc.getLocalizedString(558) :             #Album
            self._edit_db_tag(json.dumps(self._set_string(xbmc.getInfoLabel('ListItem.Album'))),self.TYPE,"album")
        elif self.modeselect[Edit_Selection] == xbmc.getLocalizedString(554) :             #TrackNumber (needs checking)
            self._edit_db_tag(self._set_string(xbmc.getInfoLabel('ListItem.TrackNumber')),self.TYPE,"track")
        elif self.modeselect[Edit_Selection] == xbmc.getLocalizedString(20416) :             #firstaired (needs checking)
            self._edit_db_tag(json.dumps(self._set_string(xbmc.getInfoLabel('ListItem.Premiered'))),self.TYPE,"firstaired")       
        elif self.modeselect[Edit_Selection] == xbmc.getLocalizedString(21893) :             #born
            self._edit_db_tag(json.dumps(self._set_string(xbmc.getInfoLabel('ListItem.Property(Artist_Born)'))),self.TYPE,"born")
        elif self.modeselect[Edit_Selection] == xbmc.getLocalizedString(21893) :             #formed
            self._edit_db_tag(json.dumps(self._set_string(xbmc.getInfoLabel('ListItem.Property(Artist_Formed)'))),self.TYPE,"formed")
        elif self.modeselect[Edit_Selection] == xbmc.getLocalizedString(21821) :             #description
            self._edit_db_tag(json.dumps(self._set_string(xbmc.getInfoLabel('ListItem.Property(Artist_Formed)'))),self.TYPE,"description")
        elif self.modeselect[Edit_Selection] == xbmc.getLocalizedString(21897) :             #died
            self._edit_db_tag(json.dumps(self._set_string(xbmc.getInfoLabel('ListItem.Property(Artist_Died)'))),self.TYPE,"died")
        elif self.modeselect[Edit_Selection] == xbmc.getLocalizedString(21896) :             #disbanded
            self._edit_db_tag(json.dumps(self._set_string(xbmc.getInfoLabel('ListItem.Property(Artist_Disbanded)'))),self.TYPE,"disbanded")
        elif self.modeselect[Edit_Selection] == xbmc.getLocalizedString(21898) :             #yearsactive
            self._edit_db_tag(json.dumps(self._set_string(xbmc.getInfoLabel('ListItem.Property(Artist_YearsActive)'))),self.TYPE,"yearsactive")
        elif self.modeselect[Edit_Selection] == xbmc.getLocalizedString(569) :             #comment
            self._edit_db_tag(json.dumps(self._set_string(xbmc.getInfoLabel('ListItem.Property(Artist_YearsActive)'))),self.TYPE,"comment")
        elif self.modeselect[Edit_Selection] == xbmc.getLocalizedString(175) :             #mood
            moodstring = self._set_string("")
            self._edit_db_tag(json.dumps(moodstring.split( ' / ' )),self.TYPE,"mood")
        elif self.modeselect[Edit_Selection] == xbmc.getLocalizedString(176) :             #style
            stylestring = self._set_string("")
            self._edit_db_tag(json.dumps(stylestring.split( ' / ' )),self.TYPE,"style")
        elif self.modeselect[Edit_Selection] == xbmc.getLocalizedString(176) :             #Instruments
            instrumentstring = self._set_string("")
            self._edit_db_tag(json.dumps(instrumentstring.split( ' / ' )),self.TYPE,"instrument")
        elif self.modeselect[Edit_Selection] == xbmc.getLocalizedString(21895) :             #themes
            themestring = self._set_string("")
            self._edit_db_tag(json.dumps(themestring.split( ' / ' )),self.TYPE,"theme")
        self._select_dialog()
            
    def _set_string( self,preset ):
        keyboard = xbmc.Keyboard(preset)
        keyboard.doModal()
        if (keyboard.isConfirmed()):
            return keyboard.getText()
        else:
            return ""
            
    def _AddToList( self, Label, identifier ):
        self.modeselect.append(Label)
        self.identifierlist.append(identifier)    
        
    def _edit_db_tag( self,genre,type,label ):
        if ((type == "Song") or (type == "Album") or (type == "Artist")):
            xbmc.executeJSONRPC('{"jsonrpc": "2.0", "id": 1, "method": "AudioLibrary.Set%sDetails", "params": { "%s": %s, "%sid":%s }}' % (type,label,genre,type.lower(),self.DBID))
        else:
            xbmc.executeJSONRPC('{"jsonrpc": "2.0", "id": 1, "method": "VideoLibrary.Set%sDetails", "params": { "%s": %s, "%sid":%s }}' % (type,label,genre,type.lower(),self.DBID))
                
if ( __name__ == "__main__" ):
    Main()
log('finished')
