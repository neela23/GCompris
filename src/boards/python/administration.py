# Administration Board module
import gnome
import gnome.canvas
import gcompris
import gcompris.utils
import gcompris.skin
import gtk
import gtk.gdk
from gettext import gettext as _

# To add a panel, add a python module in the admin subdir
# This module must have a start() and end() function
# Also add it in admin/__init__.py
# Add it in the "from import" bellow
# Last add it in the self.modules variable
from admin import users
from admin import profiles

class Gcompris_administration:
  """Administrating GCompris"""


  def __init__(self, gcomprisBoard):
    self.gcomprisBoard = gcomprisBoard

    # The panel being displayed
    self.current_panel = None

    # Create our rootitem. We put each canvas item in it so at the end we
    # only have to kill it. The canvas deletes all the items it contains automaticaly.
    self.rootitem = self.gcomprisBoard.canvas.root().add(
      gnome.canvas.CanvasGroup,
      x=0.0,
      y=0.0
      )
                    
    gap = 10
    panel_x = 120
    self.select_area = (gap , gap, panel_x + gap , gcompris.BOARD_HEIGHT-gap)
    self.panel_area  = (panel_x + 2*gap , gap, gcompris.BOARD_WIDTH-gap, gcompris.BOARD_HEIGHT-gap)

    print("Gcompris_administration __init__.")


  def start(self):
    self.gcomprisBoard.level=1
    self.gcomprisBoard.maxlevel=1
    self.gcomprisBoard.sublevel=1
    self.gcomprisBoard.number_of_sublevel=1
    gcompris.bar_set(0)
    gcompris.set_background(self.gcomprisBoard.canvas.root(),
                            gcompris.skin.image_to_skin("gcompris-bg.jpg"))
    gcompris.bar_set_level(self.gcomprisBoard)

    self.rootitem.add(
      gnome.canvas.CanvasRect,
      x1=self.select_area[0],
      y1=self.select_area[1],
      x2=self.select_area[2],
      y2=self.select_area[3],
      fill_color="white",
      outline_color_rgba=0x111199FFL,
      width_units=1.0
      )

    self.rootitem.add(
      gnome.canvas.CanvasRect,
      x1=self.panel_area[0],
      y1=self.panel_area[1],
      x2=self.panel_area[2],
      y2=self.panel_area[3],
      fill_color="white",
      outline_color_rgba=0x111199FFL,
      width_units=1.0
      )

    # Display the menu in the selection area
    # The list of modules
    i = 0
    users.Users(self.rootitem).init(i, self.select_area, self.select_event)
    i+=1
    profiles.Profiles(self.rootitem).init(i, self.select_area, self.select_event)
    
    print("Gcompris_administration start.")


  def end(self):
    print("Gcompris_administration end.")


  def ok(self):
    print("Gcompris_administration ok.")


  def repeat(self):
    print("Gcompris_administration repeat.")


  def config(self):
    print("Gcompris_administration config.")


  def key_press(self, keyval):
    #print("Gcompris_administration key press. %i" % keyval)
    return gtk.FALSE

  # ---- End of Initialisation

  # Event when a tool is selected
  def select_event(self, item, event, module):
    if event.type == gtk.gdk.BUTTON_PRESS:
      if event.button == 1:

        # Do not reload it
        if(self.current_panel ==  module):
          return
        
        # Stop previous panel if any
        if(self.current_panel != None):
          self.current_panel.stop()
          
        self.current_panel = module

        # Start the new panel
        module.start(self.panel_area)
        