# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os
import re
import socket
import subprocess
from libqtile import hook
from libqtile import qtile
from typing import List  # noqa: F401
from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile.widget import Spacer, Backlight
from libqtile.widget.image import Image
from libqtile.dgroups import simple_key_binder


#My programmes
mod = "mod4"
myBrowser = 'firefox'
myTerminal = 'kitty'
myTextEditor = 'geany'
myPrimaryFileManager = 'kitty vifm'
mySecondaryFileManager = 'pcmanfm'
myRecorder = 'obs'
myDrawingApp = 'mypaint'
myVideoEditor = 'kdenlive'
myAudioEditor = 'audacity'
myPhotoEditor = 'gimp'
myVirtualbox = 'virtualbox'
myVideoPlayer = 'vlc'
myPrimaryMenu = 'rofi -show run'
mySecondaryMenu = 'dmenu_run'
myEmailCliant = 'thunderbird'




keys = [
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc = "Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc = "Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc = "Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc = "Move focus up"),
    Key([mod], "space", lazy.layout.next(),
        desc = "Move window focus to other window"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "j", lazy.layout.shuffle_left(),
        desc = "Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(),
        desc = "Move window to the right"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_down(),
        desc = "Move window down"),
    Key([mod, "shift"], "i", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(),
        desc = "Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(),
        desc = "Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(),
        desc = "Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc = "Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc = "Reset all window sizes"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
        desc = "Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn(myTerminal), desc = "Launch terminal"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc = "Toggle between layouts"),
    Key([mod, "shift"], "c", lazy.window.kill(), desc = "Kill focused window"),

    Key([mod, "control"], "r", lazy.restart(), desc = "Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc = "Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(),
        desc = "Spawn a command using a prompt widget"),

    #Browser
    Key([mod], "b", lazy.spawn(myBrowser), desc = "Launch browser"),

    #Geany
    Key([mod], "t", lazy.spawn(myTextEditor), desc = "Launch geany"),

    #Email cliant
    Key([mod], "e", lazy.spawn(myEmailCliant), desc = "Launch thunderbird"),

    #Primary File manager
    Key([mod], "f", lazy.spawn(myPrimaryFileManager), desc = "Lauch primary file manager"),
    
    #Secondary File manager
    Key([mod, "shift"], "f", lazy.spawn(mySecondaryFileManager), desc = "Lauch secondary file manager"),

    #rofi
    Key([mod], "space", lazy.spawn(myPrimaryMenu), desc = "Launch rofi"),
    
    #dmenu
    Key([mod], "d", lazy.spawn(mySecondaryMenu), desc = "Launch demnu"),

    #open qtile config.py
    Key([mod, 'c'], 't', lazy.spawn(myTerminal + 'vim .config/qtile/config.py'), desc='Open qtile configuration file'),

    #Sound
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pactl set-sink-volume 0 +5%")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("pactl set-sink-volume 0 -5%")),
    Key([], "XF86AudioMute", lazy.spawn("pactl set-sink-mute 0 toggle")),

    #Brightness
    Key([], "XF86MonBrightnessUp", lazy.spawn("lux -a 10%")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("lux -s 10%")),
]

groups = [Group("", layout='bsp', matches=[Match(wm_class=myBrowser)]),
          Group("", layout='bsp'),
          Group("", layout='bsp', matches=[Match(wm_class=myTextEditor)]),
          Group("", layout='bsp', matches=[Match(wm_class=mySecondaryFileManager)]),
          Group("", layout='bsp', matches=[Match(wm_class=myRecorder)]),
          Group("", layout='bsp', matches=[Match(wm_class=myDrawingApp)]),
          Group("", layout='bsp', matches=[Match(wm_class=[myVideoEditor, myAudioEditor, myPhotoEditor])]),
          Group("", layout='bsp', matches=[Match(wm_class=myVideoPlayer)]),
          Group("", layout='bsp', matches=[Match(wm_class=myVirtualbox)]),
          Group("", layout='bsp')]

dgroups_key_binder = simple_key_binder(mod)

colors = [["#282a36", "#282a36"],  #background (dark grey) [0]
          ["#44475a", "#44475a"],  #light grey [1]
          ["#f8f8f2", "#f8f8f2"],  #forground (white) [2]
          ["#6272a4", "#6272a4"],  #blue/grey) [3]
          ["#8be9fd", "#8be9fd"],  #cyan [4]
          ["#50fa7b", "#50fa7b"],  #green [5]
          ["#ffb86c", "#ffb86c"],  #orange [6]
          ["#ff79c6", "#ff79c6"],  #pink [7]
          ["#bd93f9", "#bd93f9"],  #purple [8]
          ['#ff5555', '#ff5555'],  #red [9]
          ["#f1fa8c", "#f1fa8c"]]  #yellow [10]

layouts = [
    layout.Bsp(border_focus = colors[8], margin = 2),
    layout.RatioTile(border_focus = colors[8], margin = 2),
    layout.TreeTab(border_focus = colors[8], margin = 2),
    layout.Tile(border_focus = colors[8], margin = 2),
    #layout.Floating(border_focus='bd93f9', margin = 4),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    #layout.Matrix(),
    #layout.MonadTall(),
    #layout.MonadWide(),
    #layout.RatioTile(),
    #layout.Tile(),
    #layout.TreeTab(),
    #layout.VerticalTile(),
    #layout.Zoomy(),
]

widget_defaults = dict(
    font = 'Ubuntu Bold',
    fontsize = 12,
    padding = 2,
    background = colors[0]
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top = bar.Bar(
            [
                widget.Image(
                    filename = '~/.config/qtile/icons/python.png',
                    scale = 'False',
                    margin_x = 5,
                    mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(mySecondaryMenu)}
                    ),
                widget.Sep(
                    linewidth = 2,
                    padding = 5,
                    foreground = colors[2]
                    ),
                widget.GroupBox(
					margin_x = 5,
					active = colors[2],
                    inactive = colors[1],
                    highlight_color = ["#282a36", "#bd93f9"],
                    highlight_method = 'line',
                    ),
               widget.Prompt(),
               widget.CurrentLayoutIcon(
					scale = 0.7
					),
               widget.Sep(
                    linewidth = 2,
                    padding = 5,
                    foreground = colors[2]
                    ),
               widget.WindowName(
				    foreground = colors[5]
                    ),
                widget.Chord(
                    chords_colors = {
                        'launch': ("#ff5555", "#f8f8f2"),
                    },
                    name_transform=lambda name: name.upper(),
                    ),
                widget.Systray(),
                widget.Sep(
                    linewidth = 2,
                    padding = 5,
                    foreground = colors[2]
                    ),
                widget.Net(
                    interface = "wlp4s0",
                    format = '  {down} ↓↑ {up}',
                    padding = 10,
                    mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerminal + ' -e nmtui')},
                    foreground = colors[7]
                    ), 
                widget.Sep(
                    linewidth = 2,
                    padding = 5,
                    foreground = colors[2]
                    ),
                widget.CPU(
                format = '  {freq_current}GHz {load_percent}%',
                padding = 10,
                mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerminal + ' -e htop')},
                foreground = colors[10]
                ),
                widget.Sep(
                    linewidth = 2,
                    padding = 5,
                    foreground = colors[2]
                    ),               
				widget.Memory(
                    foreground = colors[4],
                    mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerminal + ' -e htop')},
                    fmt = '  {}',
                    padding = 10
					),
                widget.Sep(
                    linewidth = 2,
                    padding = 5,
                    foreground = colors[2]
                    ),
				widget.ThermalSensor(
                       foreground = colors[9],
                       background = colors[0],
                       threshold = 70,
                       fmt = '  {}',
                       padding = 10
                       ),
                widget.Sep(
                    linewidth = 2,
                    padding = 5,
                    foreground = colors[2]
                    ),
                widget.Volume(
					fmt = '  {}',
					foreground = colors[8],
					padding = 10
					),
				widget.Sep(
                    linewidth = 2,
                    padding = 5,
                    foreground = colors[2]
                    ),
                widget.Battery(
                        charge_char ='',
                        discharge_char = '',
                        format = '  {percent:2.0%} {char}',
                        foreground = colors[6],
                        padding = 10
                    ),
                widget.Sep(
                    linewidth = 2,
                    padding = 5,
                    foreground = '#ffffff'
                    ),
                widget.Clock(format=' %a %d %m %Y |  %I:%M %p',
					foreground = colors[2],
					padding = 10
					),
				widget.Sep(
                    linewidth = 2,
                    padding = 5,
                    foreground = '#ffffff'
                    ),
				widget.QuickExit(
					fmt = ' ',
					foreground = colors[9],
					padding = 10
					),              
            ],
            20,
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start = lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start = lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

#dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class = 'kdenlive'),  # gitk
    Match(wm_class = 'gimp'),  # gitk
    Match(wm_class = 'mypaint'),  # gitk
    Match(wm_class = 'ssh-askpass'),  # ssh-askpass
    Match(title = 'branchdialog'),  # gitk
    Match(title = 'pinentry'),  # GPG key password entry
])
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

#Programms to start on log in
@hook.subscribe.startup_once
def autostart ():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.call([home])

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
