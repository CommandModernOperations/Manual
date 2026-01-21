#  11.0 Appendices

## 11.1 Keyboard Commands

This is a listing of various hotkey commands that can also be accessed
in-game via the Help drop-down menu. For KEYPAD commands, Num Lock must
be off.

**Basic**

Spacebar, CTRL+ENTER: Pause/Resume Game.

CTRL+S: Save Scenario.

**Tactical Map**

CTRL+ [1...0] Store quick-jump slot

[1...0] Recall quick-jump slot.

Mouse Right-Click: Center map on clicked point

Mouse Right-Click and drag: Pan map

Up arrow, Num 8: Pan map up

Right arrow, Num 6: Pan map right

Left arrow, Num 4: Pan map left

Down arrow, Num 2: Pan map down

Z, Mouse Scroll: Zoom in

X, Mouse Scroll: Zoom out

V, PgUp, Num 9: Switch unit/group view

\| (vert separator): Select next unit

Backspace: Select previous unit

T Track selected unit

Del Delete selected waypoint

CTRL+Ins Add reference point

CTRL+R Rename Reference Point

CTRL+Del Delete Reference Point

CTRL+End Deselect All Reference Points

CTRL+D Range/Bearing Tool

End, Num 1 Toggle Illumination Vectors

Home, Num 7 Toggle Targeting Vectors

\* (Star) Toggle Datablocks

CTRL+M Clear Message Log

CTRL+Shift+M Message Log in Separate Window

**Scenario Editor**

CTRL+V Toggle God's Eye View (see all)

INS Add Unit

C Copy Unit

Shift+C Clone Unit

M Move Unit

R Rename Unit

Del Delete Unit

Alt+S Toggle Sides

CTRL+X Map coordinates to clipboard

CTRL+F6 Add/Remove Aircraft

CTRL+F7 Add/Remove Boats

**Function Keys**

F1 Engage Targets (Auto)

Shift+F1 Engage Targets (Manual)

CTRL+F1 Bearing Only Launch

F2 Throttle+Altitude

F3 Plot Course

F4 Formation Editor

F5 Magazines

F6 Air Operations

F7 Boat Operations

F8 Mounts + Weapons

F9 Sensors

CTRL+F9 Unit/Group Doctrine

CTRL+Shift+F9 Side Doctrine

F10 Damage/Systems Status

F11 Mission Editor

CTRL+F11 Create New Mission

**Own Units**

U Unassign Selected Units, including missions and RTB state

G Group Selected Units

D Detach Selected Units From Group

A Toggle Weapons Hold/Inherit for Selected Units

CTRL+A Toggle Weapons Hold/Inherit for All Units

I Toggle Ignore Plotted Course When Attacking For Selected Unit

CTRL+I Toggle Ignore Plotted Course When Attacking For All Units

E Drop Target

CTRL+E Disengage (Drop All Targets)
L Hold Position For Selected Units

CTRL+L Hold Position For All Units

Shift+ [ Drop Passive Sonobuoy Above Layer

[ Drop Passive Sonobuoy Below Layer

Shift+ ] Drop Active Sonobuoy Above Layer

] Drop Active Sonobuoy Below Layer

Shift+D Deploy Dipping Sonar

O Display Order of Battle+Contacts Window

**Contacts**

P, PgDn, Num 3 Drop Contacts

H Mark Hostile

CTRL+H Mark Unfriendly

N Mark Neutral

F Mark Friendly

R Rename

**Misc**

CTRL+Shift+C Lua Script Console

CTRL+C Copy Lua values of selected unit to clipboard

CTRL+Z Copy Lua values of highlighted RPs to clipboard

## 11.2 Custom Overlays 101

To add overlays to command you must first use third party software to
generate geo-referenced files and then you can upload them to your
command using an in-game interface.

For demonstration purpose we are using a modified GMAP as we've had good
experiences with it. We do not guarantee its future functionality nor
are we in any way responsible for the accuracy of the open-source
imagery.

Download the modified GMAP
(<http://www.matrixgames.com/forums/tm.asp?m=3530108/>) and unzip to a
location you'll be able to find.

To run the program, click the Demo.WindowForms.exe file.

When launched you can manipulate the map with your mouse and change the
imagery type using type drop down. In general, it is best to find what
you're looking for using maps and then go to the satellite imagery
(Google satellite, Bing, etc.) to actually take the picture. I would
even suggest going to Google Earth or finding the exact coordinates in
Google first to save some time. You can also overlay any of these map
types although the satellite imagery looks best.

Keep imagery small (no larger than a city) to avoid potentially serious
stability and performance issues.

When you're ready to capture something to use as a file:

1\. Press the Alt button and left click mouse drag the area you would
like to capture. You'll know you're successful when it is highlighted
with a blue box. When satisfied that you've captured what you want then
press the get static button on the right.

2\. When the static map maker dialog appears:

a\. Set the Zoom level to 17

b\. Check the Make Worldfile check box

c\. Push the Generate button

3\. When complete you'll notice that two files have been generated; one
is a .png and the other is a .pgw.

4\. You can further edit the files in any image editing program if you
choose.

5\. To import into COMMAND, launch the game, create your side and click
the Custom Overlay button and when the Custom Layer Manager appears
press the Add Layer button. This will launch Windows Add File dialog.

Please choose the .png file and allow the display time to load. Once
loaded, you will see it in the bottom list. The most recent overlay will
be highest on the list.

To remove an overlay, simply select it in the Custom Layer Manager and
press the Remove Selected Button.

## 11.3 Database Edit Capability in the Scenario Editor

COMMAND offers several tools to allow users to edit facilities and naval
units in the game. Users can add weapons mounts to a facility or naval
unit by pressing the "Add Mount" button in the weapons dialog.

This launches the Add weapons dialog.

**To add a weapon**:

1\. Search for the weapon you would like in the mount list at the
bottom. To sort the list, click on the column headers (ID or Name). You
can also filter by a search term by checking off the filter by keyword
check box and entering text in field above the mount list. Once you find
the mount you would like to add select it.

2\. Use the arcs checkbox diagram to select the weapon's firing arc. If
you'd like 360 coverage, check them all off. Photographs of similar
weapons give a good idea for how the arc is like. Surface-to-surface
missile launchers tend to have narrow arcs, while forward-mounted gun
turrets cannot engage in the rear of the ship.

3\. Press the "Add Selected" button and now the weapon will appear in
the weapons dialog.

**To remove a weapon**:

1\. Select the weapon in the weapons dialog.

2\. Press the remove mount button. The weapon should now be removed from
your list.

Users can also change the weapons within an existing mount by removing
existing weapons records and adding new weapons records. You can do this
by:

- Selecting the weapon's record, you would like to remove by selecting
  it and pressing the "Remove Weapon Record" button.

- Pressing the "Add Weapon Record" button which will display the "Add
  Weapon Record" dialog.

To search for a record, you can click on the table header, or you can
filter by keyword by checking off the Filter by keyword checkbox and
typing in a text term in the provided text box.

To select a weapon's record select it within the list in press the Add
selected button.

**Adding Sensors**

Users can add a sensor to a naval unit or facility by pressing the "Add
Sensor" button in the Sensors dialog.

**NOTE**: To add a new magazine to a unit you will need to add it with a
configuration file. You can find instructions on that in sections
7.1.6-7.1.9 of the game manual.

**To Add a Sensor**:

1\. Search for the sensor you would like in the mount list at the
bottom. To sort the list click on the column headers (ID or Name). You
can also filter by a search term by checking off the filter by keyword
check box and entering text in field above the sensor list. Once you
find the mount you would like to add, select it.

2\. Use the ARCS checkbox diagram to select the sensors detection and
tracking/illumination arcs. If you'd like 360 coverage, check them all
off.

3\. Press the "Add Selected" button and now the sensor will appear in
the sensors dialog.

**To Remove a Sensor**:

1\. Select the sensor in the sensors dialog.

2\. Press the "Remove Mount" button. The sensor should now be removed
from your list.

And remember...

When making changes, the important thing to remember is that any "full"
scenario rebuild will delete your edits. To retain them you'll need to
add changes to a scenario configuration file. You can do this by
generating a so-called "delta file" which shows the changes from the
"stock" configurations and then applying them to the configuration file.
Specific instructions on how this works can be found in sections 7.1.6-
7.1.9. Keep in mind that our DB editors always reserve the right to
change record numbers, so it is best to keep up with changes.


