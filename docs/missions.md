# 7.0 Missions, Cargo Missions, Operations Planning, and Reference Points

Missions and reference points are the vital building blocks of COMMAND.
Learning how to use them is essential for both playing and creating
scenarios.

### 7.0.1 What are missions, and what are they for

Missions are tasks that platforms or groups of platforms can be
assigned. The various mission types can have sub-types and their own
Doctrine/ROE and EMCON settings. Missions are either Area Oriented or
Task Oriented. Area Oriented missions such as Patrol Missions are
defined by Reference Points, Task oriented missions such as Strike are
defined by target units.

Missions are one of the fundamental simulation constructs in Command,
both from a UI perspective and from a simulation engine point of view.
They provide three key elements:

1)  **Abstraction of control:** Without missions, a player/user has to
    issue precise instructions to each and every unit present in a
    scenario and must also update those orders as the situation changes.
    This can easily grow into micromanagement hell in a scenario with
    thousands of units to control. Units under mission tasking will
    independently navigate, move, change their EMCON settings, detect,
    engage the enemy and withdraw to host bases (if applicable) under
    their mission AI logics.

2)  **Control & behavior of units not under human control:** When using
    Command in single-player mode, it is necessary to "program"
    non-friendly units in order to instruct their behavior. Again,
    precise instructions are tedious to issue and can rapidly become
    outdated as the tactical/operational picture develops. Missions
    allow issuing general directions to computer-controlled units and
    then have them execute them on their own accord.

3)  **Behavior variability:** Giving precise manual orders means the
    units will follow them to the letter (unless disrupted by the enemy,
    the weather, the environment etc.). This is often undesired as it
    makes their behavior too predictable. Units operating under a
    mission tasking will display greater variability in the execution of
    their mission.

## 7.1 Mission Editor

The mission editor provides a list of all current missions, and it also
gives you the ability to create, edit and manage them. You can access it
from the toolbar by pressing the mission editor button or by pressing
F11 on your keyboard.

![A screenshot of a computer program Description automatically
generated](D:/dev_command/Manual/workspace/images/media/image105.png){width="7.5in"
height="4.7131944444444445in"}

The mission editor is separated into three major tabs: units, mission
settings and targets. Each page allows you customize the behavior of
your missions as well as the relevant target assignment, formation
settings and flight characteristics. When adding units to a mission, the
type of loadout for each unit is displayed next to the unit to make it
easier to identify which units you wish to use on a given mission.

![](D:/dev_command/Manual/workspace/images/media/image106.png){width="2.8541666666666665in"
height="0.25in"}

### 7.1.1 Adding a new Mission

To create a new mission, click on the Add button in the upper right
corner of the dialog. Alternatively, you may press CTRL+F11 in the main
game window to bring up the dialog. You also have the options to clone
an existing mission by highlighting and pressing clone or deleting an
existing mission by highlighting it and pressing delete.

![](D:/dev_command/Manual/workspace/images/media/image107.png){width="2.6354166666666665in"
height="1.6354166666666667in"}

A box will appear allowing you to set the basics properties of your new
mission.

![](D:/dev_command/Manual/workspace/images/media/image108.png){width="5.0in"
height="2.3333333333333335in"}

The category of the mission refers to what type of mission you are
planning to execute. Each category has a unique purpose:

Mission: This refers to your standard mission that various units can be
assigned to. They are generally 'one-off' style operations that can be
continuous but not easily repeated.

Task Pool: This is where you can define a group of units for the
purposes of completing packages. Once a unit is added to the task pool,
it can be assigned package missions.

Package: This type of mission refers to a single package in a larger
mission and unlike regular missions, it requires units to be assigned to
the task pool before it can be started.

Once you have selected the category of mission, you can select an
appropriate name and class.

![](D:/dev_command/Manual/workspace/images/media/image109.png){width="4.8541994750656166in"
height="2.34375in"}

Mission classes are described later on in the documentation. Once the
class is selected, then the type of mission is selected. Note that for
strike type missions, the targets that are selected must match the class
of mission for them to be completed properly.

After selecting the different types, a mission can be set of active
meaning it will launch as soon as practical or inactive meaning that it
will need to be activated later in order to start the mission. Task
pools and packages do not have activation times and will have to be
manually activated at a later time. Note that cargo missions that
feature airdrops can be assigned into these groups so that you have more
control over the various dropping units.

![](D:/dev_command/Manual/workspace/images/media/image110.png){width="2.0208333333333335in"
height="2.0625in"}

When setting activation and deactivation time it is important to note
that the times are listed in Zulu time and not local. Below the
activation time window are options when the mission ends to:

Unassign Units -- Remove all the units from this mission when it is over
and put them back in the available aircraft pool after the mission is
deactivated.

Order RTB -- Order all units on this mission to return to base after the
mission has deactivated

Delete Mission -- Remove the mission from the mission list after it is
deactivated.

Once the mission is created, the next steps are typically to set up
appropriate times, doctrine and bases if required. Typically, time on
target and takeoff times should be set after all the appropriate
aircraft are assigned and other mission settings are developed. If
multiple types of units are given the same time on target (such as ships
with cruise missiles and aircraft with bombs), the units will reserve
the attack so that they will not fire until they can strike the target
as close to the same time as possible3.

![](D:/dev_command/Manual/workspace/images/media/image111.png){width="1.4375in"
height="5.0in"}

The next step in building a mission is selecting the appropriate units
from the available list and then pressing the down arrow. You can filter
the visible units by pressing the appropriate icon at the top of the
available units\' page. If you wish for a unit to be available for
multiple missions, you can select that unit and then press the Dynamic
button in the top right of the page. Once this pressed, the unit will
remain available for tasking when 'Showing Multi-Mission\' is selected
regardless if it is engaged in a current mission. This is a powerful
feature and requires careful timing to ensure the unit will be available
properly loaded and configured at the moment it is required in a later
mission.

**Multi-mission units** require you to select the unit and then click
the checkbox next to the Dynamic\[?\] button. Once a unit is declared
multi-mission, a list of the missions it is assigned to becomes
available underneath this checkbox on the right side of the screen. If a
unit is used in a multi-mission situation, the other queued missions
will not be triggered until the previous ones have been marked as
satisfied.

![](D:/dev_command/Manual/workspace/images/media/image112.png){width="1.9166666666666667in"
height="2.1979166666666665in"}

Note that for a multi-mission unit to be able to go onto new missions,
the previous missions must be completed or satisfied.

At the middle of the unit\'s page there are options to filter the units
on the mission as well as:

**Ready Selected ACs**: Selecting a checkbox next to an aircraft in the
list and pressing this button calls the ready aircraft dialog. This
allows you to make quick changes to aircraft loadouts.

**Mark aircraft as escorts:** Selecting checkboxes next to aircraft
allows you to set them to be air to air or SEAD escorts within a strike
group. When you do you will notice a \[Escort\] marker in their
descriptions. Escorts are generally more useful for gun-only or early
missile age "close escort" (like the classical WWII close escort) than
for more recent scenarios with longer-range AAMs. For that period, a
separate patrol mission is recommended.

**Un-mark from escorts**: Selecting checkboxes next to aircraft set to
escort sets them to conduct normal mission behavior and not escort
behavior.

The fields, buttons and dialogs at the bottom of the dialog allow you to
change mission behaviors or parameters. Some will vary according to the
individual mission in question and are detailed in their sections.

Once the appropriate units are assigned, the mission settings tab has
several options related to the mission. This page changes depending on
the type of mission selected and each page will be described under their
respective mission type.

![A screenshot of a computer Description automatically
generated](D:/dev_command/Manual/workspace/images/media/image113.png){width="7.5in"
height="5.496527777777778in"}

A common feature of all mission settings is setting the minimum number
of units to launch the mission as well as the option to add the flights
to the air tasking order. The final tab of the mission editor page is
the targets page. This page will only show if the mission requires
targets.

![](D:/dev_command/Manual/workspace/images/media/image114.png){width="5.145833333333333in"
height="3.259027777777778in"}

Many types of missions include options to provide for aerial refueling.
Tankers for AAR can be configured in a number of ways.

**Allow**: This means units will refuel as normal, going back to tankers
whenever they reach a low fuel state.

**Allow, But not tankers refueling tankers**: This means that non-tanker
aircraft will refuel as normal but other tankers will not.

**Not Allowed**: Units on this mission will not attempt to go for
tankers when they reach low fuel.

Inherited: This goes to the current side posture.

Clicking "configure" will open the advanced tanker planner.

![](D:/dev_command/Manual/workspace/images/media/image115.png){width="6.5in"
height="3.0in"}

**Use nearest tanker with enough fuel to serve**: This self-explanatory
measure will mean that the aircraft will go to the closest tanker that
can supply them.

**Use tankers assigned to specific missions**: This will open up a list
of the missions with tanker aircraft currently assigned to them, with
one being selectable. This can be used to prevent large aircraft (i.e.
heavy bombers) from quickly exhausting small tankers.

**Minimum Number of Tankers**: This will prevent the mission from
launching if the required number of tankers can't be met. It can be
further set to "minimum number of tankers airborne" or "minimum number
of tankers on station."

**Launch Mission Without Tankers in Place**: This is an extremely
high-risk option to launch combat aircraft without tankers currently
airborne. The aircraft will refuel, but only for tankers ahead of them
and not behind them. This is playing with fire, so if they crash, don't
say we didn't warn you.

**Maximum Number of Receivers in Queue Per Tanker**: This allows the
player to set limits on the number of aircraft "waiting in line" for
each tanker to prevent pileups.

**Receivers Start Looking For Tankers When Down To \_\_\_\_\_\_\_** :
This allows the player to change the fuel threshold when aircraft start
heading for tankers.

**Airborne Receivers Can Book Tankers Within....:** This allows the
player to only allow the aircraft to look for tankers within a certain
radius. This can be useful to avoid aircraft going to faraway tankers
supporting a completely different mission.

Many types of missions give the ability to select a custom speed,
altitude and depth for the types of units being used in a mission. This
can be controlled under the mission settings page

![](D:/dev_command/Manual/workspace/images/media/image116.png){width="5.0in"
height="2.9270833333333335in"}

Note that adjusting throttle may impact the maximum range of the mission
and any flight plans that were created along with the mission. The
Attack dist.: option allows you to define the desired distance to attack
a unit. Keep in mind that needs to agree with the WRA of the unit as
well as weapons' limitations.

## 7.2 Mission Definitions and Details

AI-controlled missions are tasks that platforms or groups of platforms
can be assigned. The various mission types can have sub-types and their
own Doctrine and EMCON. Missions are either Area Oriented or Task
Oriented. Area Oriented missions such as Patrol Missions are defined by
Reference Points, Task oriented missions such as Strike are defined by
target units, Reference Points (area)

Selecting a zone/area-based mission in the mission editor will show an
outline of the mission area on the map.

![](D:/dev_command/Manual/workspace/images/media/image117.png){width="3.9895833333333335in"
height="1.8541666666666667in"}

Missions that are area based may be defined by selecting the appropriate
reference points on the map, or if preferred, the pick area button may
be selected in the missions setting page. Once this is selected, a menu
appears with areas that can be picked for the mission. Note that if any
existing reference points are selected, this may cause the areas to
'join' each other.

### 7.2.1 Ferry Mission

A Ferry Mission transfers an air unit from one location to another. The
destination for a Ferry Mission is always a Unit, Facility, or Base that
can house the unit to be ferried. This can include friendly and neutral
air facilities. Ferry missions are highly useful for simulating civilian
air traffic or "escape" missions like the Iraqi Air Force's flight to
Iran in 1991.

**To create a ferry mission:**

> 1\. Select the destination unit or facility
>
> 2\. Add a new mission and when the dialog launches add a mission name
> and select the ferry mission type. Click the ok button which will
> launch the mission editor.
>
> 3\. Assign the desired units to the mission
>
> 4\. Set the Mission Doctrine/RoE/EMCON settings by pressing the button
> and adjust the desired altitude/speed under the "mission altitude"
> window (a routine commercial flight is going to be flying higher and
> slower than a lower altitude escape).
>
> 5\. Set the Ferry Mission specific settings "Ferry Behavior":

a\. One-Way: The mission will execute one time and will automatically
scrub once complete.

b\. Cycle: The mission will cycle between the start and destination
points after the normal turnaround time for that unit at each end.

c\. Random: The mission will randomly trigger a cycle.

**Ferry Mission Settings:**

**Ferry Behavior:** This allows the mission designer to choose between
round-trip cycles or ordinary one-way trips. If "One way" is selected,
the unit will stay at the destination base after it arrives there. If
"Cycle" is selected, the unit will arrive at the destination base,
ready, leave the destination base once its ready time has elapsed, move
back to its original base, then ready, then move back to the destination
base.

"Random" randomizes what type of ferry behavior the unit will use.

### 7.2.2 Support Mission

Support missions allow players to assign specific units to follow
waypoint-driven paths. They are most useful for AEW (airborne early
warning), Refueling (air to air refueling) and reconnaissance missions.

**To create a support mission:**

> 1\. Create and Select the desired Reference Points on the map.

2\. Create a new mission, select the support mission category and type
in a name for the mission. Click the OK button the launch the mission
editor.

> 3\. A line will appear on the map showing the support mission course
> (loop) path. The loop path may be adjusted by moving or editing the
> reference points.
>
> 4\. Assign the desired unit(s) to the mission.
>
> 5\. Set the Mission Doctrine/RoE/EMCON settings by pressing the button
> and set the desired throttle/altitude settings.
>
> 6\. Set the Support Mission specific settings:
>
> · 1/3 RULE: If checked, will keep 1/3 of the available aircraft
> airborne if possible.
>
> · ONE-TIME ONLY: The mission will execute one time only and will be
> deleted and assigned units freed after completion.
>
> · Navigation Type:
>
> a\. Continuous Loop: The A/C will loop around the mission's assigned
> reference points until Bingo Fuel.
>
> b\. Single Loop: The A/C will make one circuit around the mission's
> assigned reference points and return to its base.
>
> · Transit Throttle: Throttle setting for the aircraft while transiting
> to the first mission reference point. Settings are Loiter/Creep,
> Cruise, Full, Flank/AB.
>
> · Loop Throttle: Throttle setting for the aircraft while executing the
> support loop. Settings are Loiter/Creep, Cruise, Full, Flank/AB.
>
> · Mission Reference Points. Reference points may be added or deleted
> to/from the mission. To add make sure the reference points are
> selected on the map.
>
> 7\. Verify on the map the Support Mission path shown with a
> highlighted line.
>
> 8\. For tankers alone, checking the "tankers return to base after one
> refueling cycle, when queue is empty" means that tankers will refuel
> one "queue-full" of aircraft and then return to base themselves. This
> can be used to keep them out of danger or avoid using too much fuel.
>
> 9\. Likewise, for tankers, "tankers can refuel x numbers of receivers,
> rounded up to the nearest flight" (so for three receivers set at
> maximum, it will refuel two flights of two aircraft each) can be used
> to also restrain them.

**Support Mission Settings:**

**Try To Keep (\_\_\_) Units Per Class On Station:** This sets how many
units the mission will try to keep on the support track. Setting this to
0 means it will be ignored.

**1/3 Rule:** If checked, only a third of the aircraft currently
assigned to the mission will launch and stay in on the support track at
any one time. In the event of a conflict with the "Keep \_\_\_ Units On
Station" setting, the larger number prevails.

**One Time Only:** If checked, the unit will stay on the support track
as normal but then return to base and stay there once it reaches its
limits. It is not the same as a "single loop"

**Navigation Type:** "Continuous Loop" will have the unit(s) continually
moving around the support track as long as possible. "Single Loop" will
have the unit(s) move around the support track once and then return to
base.

*A tanker, AEW, or electronic warfare aircraft intended to remain on
station as long as possible should receive a continuous loop mission. A
recon aircraft making one pass should receive a single loop mission.*

### 7.2.3 Patrol Mission

A patrol mission is an area mission defined by reference points. Any
mobile unit may be assigned a patrol mission. If a facility or group is
assigned this mission, all of its A/C will be assigned this mission.
Aircraft will stay on patrol as long as their fuel is sufficient, and
their weapons fit the patrol settings. Submarines assigned to patrol
missions will, by default, not use their active radars when at periscope
depth or on the surface even if the inherited side EMCON is to emit if
possible. The EMCON can be manually changed to have them do so if
necessary (i.e. when using submarines with poor sonar against weak
opposition)

Patrol Mission Types:

· AAW PATROL: Units assigned to this mission will actively search for
and investigate/identify airborne contacts.

· ASW PATROL: Units assigned to this mission will actively search for
and investigate/identify sub-surface contacts.

· ASuW PATROL (NAVAL): Units assigned to this mission will actively
search and investigate/identify waterborne contacts.

· ASuW PATROL (GROUND): Units assigned to this mission will actively
search and investigate/identify contacts on land.

· ASuW PATROL (MIXED): Units assigned to this mission will actively
search and investigate/identify any non-submerged contact.

· SEAD PATROL: Units assigned to this mission will actively search and
engage targets emitting radar.

. SEA CONTROL PATROL: Unit assigned to this mission with actively search
and investigate/identify naval surface and undersea contacts.

**To create a patrol mission:**

> 1\. Create/select at least three reference points on the map to define
> the patrol area.
>
> 2\. Create a mission, select the patrol mission class and types from
> dropdowns, type in a name and click the OK button which will open the
> mission editor.
>
> 3\. A shaded box is shown on the map depicting the patrol area. A
> folded box or bow-tie shape is the result of the Reference Points not
> being placed sequentially around the perimeter of the desired area. It
> is best to use the right-control-click Define Area function as it will
> drop four reference points in the correct order.
>
> 4\. If desired, create a prosecution area. Create/select a second set
> of reference points, press the "prosecution area" tab, and add/remove
> them as one would for a normal patrol area. In order for the
> prosecution area to work, "Investigate Contacts Outside Patrol Area"
> must be checked.
>
> 5\. Assign appropriate units to the mission.
>
> 6\. Set the Mission Doctrine/RoE/EMCON settings by pressing the button
> and set the desired throttle/altitude settings.
>
> 7\. Set 1/3 RULE: If checked, will keep 1/3 of the available aircraft
> airborne if possible.
>
> 8\. Set "Investigate Contacts Outside Patrol Area" If checked, the
> units assigned to the mission will leave the patrol area to
> investigate/identify nearby contacts. If unchecked they will restrict
> their activities only to their defined area. If checked with the
> mission containing a prosecution area, the units will only investigate
> contacts inside said prosecution area.
>
> 9\. Set "Active Emissions Only Inside Patrol Area" If checked, the
> units will transit to the patrol area with radars off to avoid giving
> away the location of their parent unit.
>
> Note on prosecution zones vs patrol zones:

- Patrol zone is where the unit actually patrols. The unit never leaves
  the boundary of the zone while on mission.

- Prosecution zone is where it will \"prosecute\" any intruders, but it
  won\'t patrol there. It still patrols within the patrol zone boundary
  but will leave the patrol zone to investigate an intruder who enters
  the prosecution zone. Once it\'s done with that, it will return to the
  patrol zone.

- Prosecution zones are only active if "Investigate Contacts Outside
  Patrol Area" is set. This allows the unit to exit a patrol zone to
  investigate, but only within limits of the prosecution zone boundary.

- No prosecution zone and no "Investigate Contacts Outside Patrol Area"
  checked will let a unit investigate ANY contact ANY distance from the
  patrol zone boundary. The unit will leave the patrol zone, and this
  should be rarely used.

- Investigate within weapon range is exactly what it says. Regardless of
  patrol zone boundaries, the unit will investigate or attack any unit
  outside the patrol zone but within weapon range from the zone
  boundary.

> It\'s recommended that patrol and prosecution zones overlap. For a
> patrol mission that has a prosecution zone, the mission units won\'t
> be considered \'on station\' if they are outside both the patrol zone
> and the prosecution zone. For edge cases where a gap between the zones
> is desired, the mission attack distance setting should be adjusted to
> account for the distance from the nearest edge of the patrol zone to
> the furthest edge of the prosecution zone.

**Patrol Mission Settings:**

**Try To Keep (\_\_\_) Units Per Class On Station:** This sets how many
units the mission will try to keep in the patrol area. Setting this to 0
means it will be ignored.

**1/3 Rule:** If checked, only a third of the aircraft currently
assigned to the mission will launch and stay in the patrol area at any
one time. This is so that continuous coverage can happen, with some
aircraft flying and others down for readying. In the event of a conflict
with the "Keep \_\_\_ Units On Station" setting, the larger number
prevails.

**Flight/Group Size:** Determines how many units are in each
flight/group. Flights/groups will move as one "unit" on one path.

**Tankers/AAR:** Sets tanker/AAR settings, from "don't allow" to "allow,
including tankers refueling each other".

**Number of Aircraft/Units That Investigate Unknown Contacts:** This
allows the player to choose how many aircraft/boats/groups will abandon
their original patrol pattern to pursue and investigate an unknown
contact. It can range from none at all to every single deployed
unit/flight. Limiting the number of units that do this prevents
"pileups" where say, twenty F-15s enforcing a large no-fly zone all rush
to investigate an unknown obvious civilian aircraft.

**Number of Aircraft/Units That Engage Hostile Contacts**: This is like
the above but applied only to engaging targets confirmed/marked as
outright hostile. The default is all flights because of a perceived need
to "better be safe than sorry", but it can be adjusted as needed.

**Wingmen/Group Members Can Investigate/Engage Separate Contacts
within:** This sets the distance at which components of a group will
split off and interact with separate contacts. The default is a short 5
nautical miles, but it can be raised or lowered as needed.

**Movement Style:** This sets the basic nature of the patrol. "Random
Within Area" has randomly generated paths throughout the assigned "box"
of reference points and was the default patrol system used in previous
versions of COMMAND. "Repeated Loop" treats the mission reference points
as parts of a "track", much like support missions, and the map display
of a patrol mission set to "repeated loop" resembles that of a support
mission.

Unlike a support mission, a "repeated loop" patrol maintains the more
aggressive "investigate and engage if need be" (as doctrine and patrol
settings permit, of course) logic of proper patrol missions. Thus, an
exact, repeatable pattern can be generated using that method. Using a
prosecution area for a "repeated loop" patrol is recommended.

**Patrol Speed/Altitude Settings:** The aircraft altitude and speed
setting, or in the case of ships, the ship/sub speed setting box allows
the player to set specific speed/depth/altitude for transit to the
patrol zone, station setting, attack setting, the limit on attack
distance of patrol units.

![A screenshot of a computer program Description automatically
generated](D:/dev_command/Manual/workspace/images/media/image118.png){width="4.895869422572178in"
height="2.8021041119860017in"}

Attack distance lets you control how far away from a patrol mission
target the unit, while outside the patrol and prosecution zones, can be
and still engage the target. It\'s there to prevent situations like an
MPA takes off 500nm from the patrol zone and goes engaged offensive on
some sub contact in the zone, causing it to adopt attack altitude and
throttle at 500nm. It can also account for cases where there is a gap
between a patrol and prosecution zone.

The flight plan tab on the box allows the player to force generation of
a flight plan for the aircraft-based patrols. Flight plans can also be
edited from the Flight plan Editor button.

![A screenshot of a computer program Description automatically
generated](D:/dev_command/Manual/workspace/images/media/image119.png){width="4.989619422572178in"
height="2.8958541119860017in"}

The box also provides the option of placing the mission in the Air
Tasking Order (ATO) and access to the ATO display.

### 7.2.4 Strike Mission

This mission type also includes Air Intercepts. Strike missions are
attack missions with specific or categorized targets and defined
attackers. Aircraft at airbases and naval units at ports/motherships
will sortie on a strike mission and then return to base when the target
is destroyed, unlike in patrol missions. Thus, if a continuous presence
is desired, patrol missions may be more valuable than strike missions.
On the other side of the coin, if because of distance, risk, or
quick-turnaround times, a continuous presence is impossible, a strike
mission may be preferable to its patrol counterpart.

Strike Mission Types:

· AIR INTERCEPT: Units assigned to this mission will attempt to
intercept and engage the selected Air Contacts.

· LAND STRIKE: Units assigned to this mission will transit to within the
selected weapon's range and engage the selected land targets.

· NAVAL ASuW STRIKE. Units assigned to this mission will transit to
within the selected weapon's range and engage the selected surface
contacts.

· ASW STRIKE: Units assigned to this mission will transit to within the
selected weapon's range and engage the selected submerged contacts.

> **To create a strike mission against a categorized target:**
>
> 1\. Add a new mission and choose the strike mission class.
>
> 2\. Choose a mission type (air intercept, land strike, naval AsuW
> strike, ASW Strike) which defines the category of targets your unit
> will hunt for.
>
> 3\. Click OK, which will launch the mission editor.
>
> 4\. Assign appropriate units to the mission and set the desired unit
> parameters, including escorts if possible.
>
> 5\. Set the Mission Doctrine/RoE/EMCON settings.
>
> 6\. Define trigger options

Keep in mind that this mission launches against targets on a
first-detect basis. It is most useful for ASW, or intercept strikes.

**To create a strike mission against a specific target or set of
targets:**

1\. Select or group select a set of targets on the map.

2\. Add a new mission and choose the strike mission class and category
you would like to use. Click the OK button when complete which launches
the mission editor.

3\. Assign the appropriate unit to the mission. You can look in the
platform display to select the best platform and aircraft loadout to
use.

4\. Select an appropriate mission trigger.

5\. Set the Mission Doctrine/RoE/EMCON settings.

6\. Click Add Units to populate the Target List. If you'd like to remove
any units, select the entry in the list and click the Remove Selected
button.

Additionally, the mission settings page allows for further customization
of the mission and the methods of engagement.

![](D:/dev_command/Manual/workspace/images/media/image120.png){width="5.0in"
height="3.6875in"}

The options include:

**Flight Size --** This dictates how large of flights will be for the
strikers or for the escorts. If the Enforce flight size box is checked,
then a group of units smaller than the size will not launch on the
mission.

**Minimum \# of ready strike a/c required to trigger mission --** This
option sets the minimum number of units to be ready for deployment
before the mission will start.

**Maximum \# of flights allowed to fly mission --** This sets the total
number of groups to be launched on the mission. This is useful for
continuous missions where a suitable reserve number of strikers or
interceptors can be deployed after previous groups have disengaged.

**Tankers (AAR) -** This is described in 7.1.1.

**Fuel / Ordnance --** This option determines how a unit will handle
situations where it is unable to strike its target. Since the maximum
range of a unit is dictated by its payload, opting to retain ordnance at
long ranges may result in an aircraft unable to return to base without
jettisoning its load.

**Radar usage --** This allows the radar usage to be dictated based on
the scenario. The radar usage can be set to use existing EMCON, activate
radar at IP or activate radar at attack leg.

**Minimum and Maximum strike radius --** Using this allows a mission
designer to tweak the ranges that weapons are deployed. If left at zero,
the weapons will be utilized as soon as they come into the appropriate range
to do so. This is a good way to force certain weapon carriers to engage
within a set range band.

**Attack Method --** This sets what tactical maneuver should be used to
strike the target. The options range from large formations striking at
one target, to independently targeting after splitting into smaller
units before striking.

**Split Distance --** If an attack method was selected that involves
breaking a formation up to strike at multiple angles, the split distance
dictates how far from the target the formation should split up before
continuing onto the IP.

**Allow off-axis attack --** This option tells the mission editor to try
to offset the arrival positions of multiple groups to not strike from
the same direction. It can be used in conjunction or independently of
the attack method options.

**Use pre-generated flight plans only --** Checking this tells the
mission editor that the user intends to manually create and update the
flight plans for the mission and not to generate at the time the mission
is triggered.

**Include in Air Tasking Order (ATO) -** This adds the aircraft used in
this mission to the ATO.

**Air Tasking Order --** This page features all the missions and
packages currently assigned in the mission editor and is detailed in a
different section of the manual.

**Flight plan Editor --** Pressing this button will bring up the flight
plan editor. Before pressing this option, it is suggested to assign the
required flights first, then set the appropriate takeoff or time on
target.

![](D:/dev_command/Manual/workspace/images/media/image121.png){width="5.148560804899388in"
height="5.983794838145232in"}

The flight plan editor allows very careful manipulation of flight plans
including speeds, positions, altitudes and times. When using the flight
plan editor, it is suggested to press create or update flight plans in
the main Mission Settings page first to pre-generate the default flight
plans. The features of this page are below:

**Package -** This is the currently selected package or mission that is
being edited

**Flight --** This is the currently selected flight. If create or update
flight plans has not been selected, this may be empty.

**Callsign --** This is the callsign of the given flight. Changing this
will also change the name of the current flight.

**Task --** This is the currently assigned task of this flight.

Note: The flight plan generator is a very intricate mechanism. Newer
players should keep mission building and flight plans simple until they
become more experienced in complex operations.

Along the right side of the screen are several options related to flight
plans and major time control for a given unit. This is especially useful
for tweaking missions so that different groups of units are able to have
different characteristics depending on the tactical needs of the
operation.

The change a/c type and loadout page enables a greater degree of
customization for a given flight and the weapons that are carried by
it.:

![](D:/dev_command/Manual/workspace/images/media/image122.png){width="5.0in"
height="3.5625in"}

The change take-off and objective times allow for splitting off the
various timings for the given flight independent of the main mission
takeoff and target times. Selecting a unit on the main map that can be
used as a landing area allows you to change the take-off, landing and
diversion locations respectively. If the takeoff location is not the
unit\'s current location, the aircraft will be removed from the flight
plan and the option for an empty slot will be placed.

Below the change buttons is a table that provides critical information
about each unit in a flight along with several adjustable features that
can be set by selecting the appropriate waypoint and then clicking the
buttons located below. Note that if you lock a specific speed or time,
you can create a situation where an aircraft will run out of range or
time in an effort to match the desired situation. Other elements of a
waypoint can be edited by clicking on the down arrow next to their
respective option.

The buttons along the base of the flight plan editor allow for the
inserting of waypoints, deletion of waypoints, editing the various
properties and times of the waypoints and items such as doctrine and
sensor usage.

Setting up escorts is done in much the same way as the regular strikers,
the differences being in how they respond to targets that could threaten
their charges.

![](D:/dev_command/Manual/workspace/images/media/image123.png){width="5.0in"
height="3.1770833333333335in"}

Aircraft can be marked as escorts using the units page by selecting them
and clicking the appropriate button to add or remove them.

![](D:/dev_command/Manual/workspace/images/media/image124.png){width="3.4895833333333335in"
height="0.6145833333333334in"}

The unique features of the escort page are:

**Number of a/c that investigate unknown contacts --** This defines how
many aircraft will check out an unknown target detected within their
threat radius. This is a useful item to check to limit how many flights
will investigate each unknown that comes along during the mission.

**Number of a/c that engage hostile contacts --** This sets how many
flights can engage each hostile contact that is in the threat radius.

**Wingmen can investigate/engage separate contacts within --** This
variable allows you to define how far apart wingmen escorts can operate
when checking out contacts.

**Maximum threat response radius --** This defines how 'far away'
escorts can go to engage a threat to the mission.

The escort page also features a separate page for ships and submarines,
shooters and SEAD and non-shooters such as EW aircraft allowing you to
have granular control of the package sizes involved. At the base of the
page, you will find the air tasking order option as well as the use of
pre-generated flight plans, these do not affect the escorts since they
will automatically join up with the strikers on a mission.

The targets page allows you to control what targets are selected for a
given strike mission.

![](D:/dev_command/Manual/workspace/images/media/image125.png){width="5.260416666666667in"
height="3.3425568678915134in"}

All targets that have been added are located in the middle of the
screen. If more need to be added, it is simply a matter of selecting
them on the world map and then clicking the 'Add units selected on map'
button at the base of the screen. Removing targets is a matter of
clicking the target on the list and then hitting remove selected. If you
need to select multiple, you can hold shift to select them by list or
control to select them individually. At the base of the targets page are
additional options:

**Opportunity Scrambling --** This sets whether or not the strikers and
escorts will take shots at other targets along the way to the mission
area. If this is set to off, the escorts still work normally.

**Engage until shotgun --** This allows you to quickly set the
engagement parameter between shotgun (a single engagement) and
Winchester (continue engaging until the appropriate weapon is depleted).

**Targets destroyed --** This allows you to define whether to continue
the mission after the targets have been destroyed (useful if the mission
has targets added to it in situ) or to return to base immediately after
the destruction.

### 7.2.5 Mining Mission

All mining missions are defined, in terms of area, by reference points.
Units assigned to this mission will place mines randomly within the
defined area, must be capable of deploying mines, and must have mines
available.

**To Create a Mining Mission:**

1\. Create and select the reference points designating the area to be
mined. Try and find a good balance between "too small" and "too thinly
spread".

2\. Add a new mission and select the Mining Mission type.

3\. Add suitable units to the mission. The only effective units for this
mission are certain surface ships, submarines, and aircraft that are
specially equipped to dispense mines. The mine layer must also have
mines available.

4\. Set the Mission Doctrine/ RoE/ EMCON by pressing the button. Set the
throttle and altitude settings, if need be but be sure to stay within
the release parameters of the mines in question.

5\. Set 1/3 RULE: If checked, will keep 1/3 of the available aircraft
airborne if possible. Has no effect if aircraft are not assigned to the
mission.

6\. Set the "Arming Delay." This sets the amount of time before the
mines will arm after being deployed. The default setting is 2 hours.
This time allows the unit(s) laying the mines to safely exit the area.

7\. Verify the proper reference points are activated and add by pressing
the Add Points Currently Highlighted on Map button, which populates the
Edit Mining Area reference point list. You can remove any points by
selecting them in this list and pressing the Remove Selected button.

8\. Ensure that the mines are satisfactorily dropped-they can fall in
strange patterns.

### 7.2.6 Mine-Clearing Mission

All mine-clearing missions are area missions defined by reference
points. This mission type is also used to locate mines. Units assigned
to this mission will patrol their mission area hunting for mines. If
mine(s) are located, the unit(s) will maneuver in such a way to place
them in their sweep path. Only units equipped to sweep mines can do so;
note that they still risk damage during the sweep operation. Units
equipped with mine countermeasure\'s equipment will have a "MCM" button
on their information panel. MCM-capable helicopter units have a variety
of specific load-outs for detection and sweeping, some specific to a
type of mine. Not all mines are sweepable.

**Creating a Mine Clearing Mission**:

1\. Create and select the reference points designating the area to be
cleared of mines.

2\. Create a new mission, select the Mine Clearing Mission category and
type in a mission name. Click OK and the mission editor will launch.

3\. Add suitable units to the mission. The only effective units for this
mission are certain surface ships, submarines, and aircraft that are
specially equipped to detect and/or sweep mines. Some units only have a
mine-detection (not sweeping) capability and will patrol the area
attempting to detect mines. Units with minesweeping equipment will
patrol their mission area hunting for mines. ROVs embarked on a ship
assigned to the mission will automatically be added to it as well.

4\. Set the Mission Doctrine/ RoE/ EMCON by pressing the button.

5\. Set 1/3 RULE: If checked, will keep 1/3 of the available units on
station if possible.

6\. Verify the proper reference points are activated and add by pressing
the Add Points Currently Highlighted on Map button, which populates the
Edit Mine Clearing Area reference point list. You can remove any by
selecting reference points in this list and pressing the remove selected
button.

*Note: For long-term mine-clearing missions, it's important for the
scenario designer to have a port and the player to have a rotating array
of minehunters under the 1/3rd Rule. Mine removal vessels are
**expected** to be damaged from the blast of the mines, and so having a
rotating cycle of sweepers leaving when repaired and returning when
damaged is both realistic and efficient.*

### 7.2.7 Cargo Mission

Cargo missions should be used for high-unit amphibious or airborne
insertions, although the player can still manually unload if they
desire. For the AI, it is a necessity.

*Historical Note: Despite, or perhaps because of, the inherent risks and
complexity of amphibious operations, the overwhelming majority of them
after 1900 have not only succeeded but succeeded with the defenders
suffering far more than the attackers. The most likely explanation is
that the would-be attackers know this, allocate disproportionate
resources, plan extra-carefully, and only launch one if they know it
will work.*

![Graphical user interface Description automatically
generated](D:/dev_command/Manual/workspace/images/media/image126.jpeg){width="6.489584426946632in"
height="5.654290244969379in"}

There are two types of cargo missions: Delivery and Transfer.

**Delivery cargo missions** work as before, with the destination being a
zone defined by RPs on the map. This type of mission will unload cargo
into action / for use in the simulation (units will unload from cargo
onto the map where they can be given orders, etc. Ammo and fuel will
move into unit fuel records / magazines.)

**Transfer cargo missions** are for moving cargo from one holding unit
to another --from airbase to airbase, port to port, or supply facility
to airbase, etc. The cargo is not unloaded onto the map but moved from
the starting cargo source into one of the transporting units assigned to
the mission, transported to the destination, and then moved from the
transporting unit into destination unit's cargo. Creating a Transfer
cargo mission uses the same procedure as creating a ferry mission --
select a destination unit (rather than a group of reference points)
before you create the new mission.

Ships and aircraft transfer or deliver cargo from their starting host
unit. Ground units assigned to a cargo missions should start the
scenario loaded as cargo within the source unit (i.e. a ship, fixed
facility, airbase, etc.) They will automatically exit cargo and appear
on the map as soon as the mission activates, and they are within range
of the mission destination.

Cargo Mission Options

**Move All Cargo From All Available Sources**: This is a new option for
any cargo mission to move all the cargo from the available source(s).
You can click this checkbox instead of having to manually go through and
assign every possible cargo item. It also allows cargo to 'flow' through
a system of cargo missions without the sim needing to know what cargo is
/ is not going to be transferred to a cargo source by some other cargo
mission.

**Vehicles Stored in Cargo May Self-Transfer**: This is a new option
found on the 'Transfer To' tab for cargo transfer missions. Setting this
option 'on' allows ground units (not mobile facilities or other cargo)
that are assigned to the cargo mission to transport themselves from the
starting cargo source to the destination unit's cargo. They will exit
cargo onto the map, travel to the destination unit, and then enter the
cargo of the destination unit. In order for this to work the ground unit
needs to be in the mission source's cargo, assigned to the mission, AND
in the list of cargo to be transported (or you have the 'move all'
option set to on.)

(Blank space below due to graphic on next page.)

### 7.2.8 Cargo / Edit Cargo 

![Text Description automatically generated with medium
confidence](D:/dev_command/Manual/workspace/images/media/image127.jpeg){width="6.489584426946632in"
height="3.1972484689413823in"}

**Cargo Containers:** Cargo containers are added/removed from cargo the
same as other types of cargo. Once a container has been added to cargo
you can select it from the current cargo list on the left and click
'Edit Container' to put other cargo inside the selected container.

Cargo containers can contain ammunition, fuel, or user-defined contents.
User-defined contents can be assigned a name, size, and mass via the
Edit Container form. Containers are loaded and moved in the same manner
as other cargo types but can't be unloaded directly to the map as
independent entities -- they are always in cargo.

If cargo containers are moved as part of a cargo delivery mission they
will be delivered into nearby (within 2nm) existing supply-type
facilities if possible, or a new 'forward arming and refueling point'
facility will be created to hold the containers if none are available.

Fuel in cargo containers that is delivered via a cargo delivery mission
will be added as available fuel of the destination facility. This fuel
can then be used by other units to refuel.

Ammunition in cargo containers that is delivered via a cargo delivery
mission will go into the magazine of the destination facility. These can
be used to rearm other units that use the same ammunition type (NOTE!
Check the DB ID number to confirm your cargo ammunition matches the type
used by the unit you want to re-supply.)

**User-Defined Cargo**: This is a catch-all type of cargo for items the
user wishes to move and track as cargo, but which have no effect within
the Command simulation. User-defined cargo can be used to track the
movement and delivery of items like food, medical supplies, spare parts,
etc.

#### 7.2.8.1 Creating a Sequence of Cargo Missions

A single cargo mission can handle movement of cargo from the assigned
source(s) to one destination. By using the 'Move All Cargo' option the
user can create a sequence of cargo mission to ultimately move cargo
through a series of intermediate destinations and on to delivery in the
field. The 'Move All Cargo' option is required for this sort of system
as individual cargo missions do not know what cargo may be delivered to
their cargo source(s) by other cargo missions.

Implementing a full cargo routing and management system was outside the
scope of this development task, so the ability to use different missions
to route different cargo items from the same source to different
destinations is limited to 'originating' cargo sources -- i.e. those
where you know no other cargo mission will be delivering cargo TO the
cargo source.

(Blank space below due to graphic on next page.)

#### 7.2.8.2 Units of Measure in Cargo Editor

![Text Description automatically
generated](D:/dev_command/Manual/workspace/images/media/image128.jpeg){width="7.304117454068241in"
height="5.208333333333333in"}

This option will change the display values show in the Edit Cargo and
Edit Container forms to use US units of measure (feet / square feet /
tons / pounds / gallons) rather than metric units. This option applies
ONLY to those two forms. The forms will refresh automatically if change
the option.

## 7.3 Reference Points

### 7.3.1 Reference Point Basics

Reference points are markers that can be placed on the map. Reference
points are used to define mission areas, objectives, and marking
locations.

**Placing Reference Points**

You can place reference points on the game display in several different
ways:

· Pressing the Ctrl button on the keyboard and right-clicking the mouse
will give you two options that give that allow you to quickly add
reference points.

· Add reference point: Selecting this will let you select a point on the
map to drop a reference point.

· Define area: Select this will let you left click drag out an area
defined by four reference points. This is very useful in creating square
areas for missions. Defined areas may be square or circular.

· You can also place a reference point from the menu by selecting add
reference point from the Mission + Ref Points drop down menu.

**Selecting and Deselecting Reference Points**

To select and deselect reference points just click on them on the UI.
With no special properties they appear as gold diamonds when selected
and dim x's when not. You can click and drag to select more than one
reference point.

**Deleting** **Reference Points**: To delete a reference point, select
the reference point and select Delete Selected Ref Points from the
Missions and Ref. Points drop-down menu.

**Moving** **Reference Points**: If unlocked, you can move reference
points by clicking and dragging them on the map.

**Naming** **Reference Points**: By default, reference points are given
arbitrary names based on unit count when added. To rename the reference
point make sure it is the only reference point selected and press the
"R" button on your keyboard. The Rename Reference dialog should appear
allowing you to change it. If it does not, you likely have another
reference point selected.

### 7.3.2 Changing Reference Point Properties

You can change several properties of reference points in the game in the
Mission and Ref. Points drop-down.

**Making Reference Points Relative**: These properties give you the
ability to anchor reference points to moving surface unit of your or a
friendly side. These are set by selecting reference points, choosing the
property in the drop-down list and then selecting the unit or group in
the display they will be relative to. This allows you to create
mission(s) with defined areas that move relative to a certain unit or
its course, such as assigning any aircraft to a mission that protects a
moving surface unit (AAW, ASW) or units.

**Make selected Reference Points Relative (Fixed) bearing to...** :
Reference points set to this maintain their position relative to the
selected unit or group. This is useful when you know the bearing of a
known threat and want to keep a patrol between it and the selected unit
regardless of the unit's course. It is also useful for missions where
staying on station is important. Reference points that are set to this
always have an \[f\] in their name.

**Make selected Reference Point(s) relative (Rotating) bearing to ...**
: Reference points set to this maintain their position relative to the
selected unit or group's course. This is useful when you would like to
patrol ahead of a group or unit regardless of its course. Reference
points that are set to this always have an \[r\] in their names.

**Locking and Unlocking Reference Points**: You can lock and unlock
reference points in the game by selecting the reference points and
choosing the Lock and Unlock Ref. Point(s) selections in the Mission +
Ref Points drop down menu. Locked reference points appear as padlocks
are unchangeable by players in game mode.

**Delete Selected**: Deletes any selected reference point.

**De-Select All Reference Points:** Deselects any currently highlighted
reference points. Can also be made by selecting CTRL-END

## 7.4 Operations Planning

To fully comprehend this function, it is essential to have a good
knowledge of the mission editor in general, and cargo missions in
particular. Previously, in Command, a given unit could only be assigned
to a single mission. If you wanted to assign the unit to another
mission, you would have to manually unassign it from the current mission
and then assign it to a new one.

### 7.4.1 Operation Planning - Nomenclature to understand

**Triggers**

A trigger in the operation planner is a condition that gets checked each
simulated second. If the conditions are met the trigger will execute a
specific action. There are two possible actions: start a mission or tag
a mission as satisfied.

**Mission status**

A mission's status in Command can be either Active or Inactive.

Active means the mission is evaluated by the Command simulation, but it
doesn't necessarily mean that the mission serves a purpose or has units
assigned to execute it.

![Graphical user interface, application Description automatically
generated](D:/dev_command/Manual/workspace/images/media/image129.png){width="2.34375in"
height="3.213888888888889in"}Inactive means that the mission is
completely ignored by the simulation until it becomes Active.

**IMPORTANT**: It is strongly recommended to leave all missions active,
especially when working with the operation planner. Set mission as
inactive only for draft missions or manually controlled missions.

**Mission phases**

A mission phase is a new concept introduced with the operation planner
and is not related to the existing mission status.

**On Hold:**

![Graphical user interface, application Description automatically
generated](D:/dev_command/Manual/workspace/images/media/image130.png){width="6.3in"
height="1.6020833333333333in"}

The mission has not yet started, the units assigned to the mission won't
execute the mission.

**Satisfied:** The mission is considered to have achieved enough of its
objective for assigned units to consider other missions, but a satisfied
mission does not necessarily end. This tag is used for mission triggers
and for multi-mission priority.

**Running:** A running mission will have its assigned mission to execute
the mission.

**H-Hour:** In Command, H-Hour designates the date and time at which the
mission designated as the initial mission for H-Hour is to start. H-Hour
in Command isn't strictly an H-hour according to military terminology as
it can be customized without restriction.

**L-Hour:** In Command, L-Hour designates the date and time at which the
mission designated as the initial mission for L-Hour is to start. L-Hour
in Command isn't strictly an L-hour according to military terminology as
it can be customized without restriction.

### 7.4.2 Understanding the concept of dynamic units

The operations planner provides the capability for a single unit to be
assigned to multiple missions. Of course, the unit can only execute one
mission at a time, but you can now prioritize which mission it should
execute. Mission priority is set via the operation planner.

Let's assume we have a scenario where a group of aircrafts is assigned
to a patrol mission. These aircrafts should patrol an area from a given
time and then start a strike mission against a group of tanks. Without
the operation planner, the player would need to track the time and then
manually switch each aircraft to a new mission, at the right moment.
Thanks to the operation planner such behavior can be automated, and in
more complex environment, our units could even behave like a reactive
AI, aware of the simulation at the strategical level.

![](D:/dev_command/Manual/workspace/images/media/image131.png){width="6.803472222222222in"
height="2.535416666666667in"}

**[IMPORTANT!]{.underline}** A unit without "Dynamic" Checked will be
ignored by the operation planner dynamic assignment, if you want a unit
to work with operation planner's feature you **[MUST]{.underline}**
designated it as a dynamic unit.

Notice that since we have toggle "Showing Multi-Mission" we are now
allowed to assign multiple mission to a unit, they are still shown in
the "Available units" list despite having an assigned mission.

![Graphical user interface, text, application Description automatically
generated](D:/dev_command/Manual/workspace/images/media/image132.png){width="1.5729166666666667in"
height="3.5729166666666665in"}This panel on the right side of the
mission editor shows all missions assigned to this unit. The mission in
green in the one currently executed by the unit. Missions don't have an
order of execution, but a priority, which is set in the operation
planner, as we will see later.

The "Dynamic" checkbox allows the unit to be assigned to multiple
missions, units are all unchecked by default to reflect default command
behavior.

![Graphical user interface, application Description automatically
generated](D:/dev_command/Manual/workspace/images/media/image133.png){width="2.427422353455818in"
height="0.6980139982502187in"}Below the mission list we can see the
current status and phase of the mission. We will see later in the
operation planner chapter as "Phase" is a new way of managing the
mission dynamically and is closely related to multi-mission.

It is on this screen that you decide to add the unit to all of the
missions you want it assigned to. At this point you don't have worry
about priority or to select a current mission as the operation planner
will manage this for you.

In above example we see that Rafale B is assigned to both the "Air
Superiority Patrol" and "Light Tanks Destruction" missions, and the
active mission for this unit is the one in green: "Air Superiority
Patrol." Depending on the configuration of the operation planer, this
unit may automatically switch to the "Light Tanks Destruction" mission
at some point in the future.

Don't worry if the multi-mission mechanism is not entirely clear to you
yet, as the mission editor is only half the story. The next chapter on
operation planner will explain the other half.

### 7.4.3 Mobile facility vs Ground unit and Split/Merge ground units

One of the most significant capabilities brought by the operation
planner, is the possibility to have units dynamically change mission.
But not all types of units are eligible for this kind of behavior. As
part of that, it is important to understand the core difference between:

- **Ground units** as facility which is a legacy implementation where
  ground unit are assimilated as moving "facility"

- **Mobile facilities**, a new implementation, which works like others
  active units such as aircraft, ships etc....

The first hold a group of units abstractly represented as "mounts",
while the last is a fully simulated individual unit. The core difference
that interests us here is that ground units as facility are transported
as cargo which doesn't have an existence in the simulation until it has
landed (and spawned).

This means that we can't assign or queue them a mission until they have
landed, and you will not be able to achieve a fully autonomous behavior
for your units, in this case.

Since the 8th of November 2021 update, we allow cargo operation for
active units, meaning that all these limitations are now removed.
However, you must have the right methodology to achieve this.

Unless you have to achieve backward compatibility or if a database entry
is missing, **[you MUST use ground units NOT mobiles
facilities]{.underline}** to use the operation planner at its fullest.

On the new cargo edition form, note the "type", at the moment, the
database has more content for mobile

facility, fortunately, our database is expanding to have the active
ground units catch up in content with the rest.

![Graphical user interface, text Description automatically
generated](D:/dev_command/Manual/workspace/images/media/image134.png){width="6.081944444444445in"
height="3.615972222222222in"}

**Ability to Split/Merge ground units (facilities)**

Legacy ground units associated as "facilities" can now be rearranged
through this new tool.

![A screenshot of a computer Description automatically generated with
medium
confidence](D:/dev_command/Manual/workspace/images/media/image135.png){width="1.7916666666666667in"
height="1.5625in"}![A picture containing text Description automatically
generated](D:/dev_command/Manual/workspace/images/media/image136.jpeg){width="3.9166666666666665in"
height="2.9631944444444445in"}

Select an eligible unit, such as a landed detachment, right click on it
to bring the context menu and click on "Split unit".

This brings you this menu, with the details of the detachment. You can
also break the detachment into individual units with a single click.

![Graphical user interface Description automatically
generated](D:/dev_command/Manual/workspace/images/media/image137.png){width="3.91875in"
height="2.3305555555555557in"}![Text Description automatically
generated](D:/dev_command/Manual/workspace/images/media/image138.png){width="3.282638888888889in"
height="2.0652777777777778in"}

![A screenshot of a computer Description automatically generated with
low
confidence](D:/dev_command/Manual/workspace/images/media/image139.png){width="2.408333333333333in"
height="4.080555555555556in"}Two eligible units can be merge together:

## 7.5 Operation Planner 

The operation planner adds a new level of interaction between missions
and allows units to be dynamically reassigned from one mission to
another.

Since the operation planner is sometimes tied to a landing plan, we have
here the concepts of H-Hour and L-Hour to indicate overall operational
time. These can of course be ignored or used in a different purpose.

On the top left, are where you define the parameters for the H-Hour and
the L-Hour.

![Graphical user interface Description automatically
generated](D:/dev_command/Manual/workspace/images/media/image140.png){width="5.084044181977253in"
height="0.7605227471566054in"}

The H-Hour box on the left is where we can define the date and time to
start the H-Hour mission. The H-Hour mission is the initial mission in
the operation. L-Hour box works identically to H-Hour, but they are
independent.

Once an H-Hour or L-Hour is hit the respective initial mission can no
longer be changed.

The checkbox in the middle ties the H-Hour to the L-Hour, meaning that
the time separation will be constant between H-Hour and L-Hour when you
modify the time for either. In other words, H-hour and L-hour will match
at all times if that center check box is checked.

![Une image contenant table Description générée
automatiquement](D:/dev_command/Manual/workspace/images/media/image141.png){width="6.3in"
height="2.4in"}

The spreadsheet in the center lists all the side's missions. Most
columns are informational. Generally, you will be dealing with 2
columns: **Priority** and **Phase**.

### 7.5.1 Mission priority

The priority of a mission does NOT designate its supposed position in a
mission execution queue. It indicates to its assigned units how
important this mission is **at this moment**. The mission priority is
used by units assigned to multiple missions to decide which mission to
execute at any given time. A unit having a mission in "On Hold" phase
will not have this mission evaluated for the active mission evaluation.

### 7.5.2 Mission phases

![Une image contenant texte, capture d'écran, intérieur, plusieurs
Description générée
automatiquement](D:/dev_command/Manual/workspace/images/media/image142.png){width="6.3in"
height="2.2708333333333335in"}

A mission phase is a new concept introduced with the operation planner
extension, it is not related to the mission status and should not be
mistaken with it. Active missions can still be running to completion
even if it cycles through all phases. An active mission only stops upon
destruction of targets, end of a single patrol, units destroyed, etc. On
the other hand, a mission can satisfy its objectives relative to the Ops
Planner without the mission ending. Phases are used only in relation to
the Ops Planner.

**Waiting for trigger:** The mission may (or may not) have already
started yet but queued units won't evaluate this mission when choosing
one to be assigned to. No dynamic units will be assigned to a mission
"Waiting for Trigger".

**Satisfied:** The mission is considered to have achieved enough of its
objective for the Ops Planner to assign current assigned dynamic units
to other missions. Keep in mind that a satisfied mission does not mean
its ending. Units currently operating in an active mission will continue
to execute that mission. But dynamic units waiting to take off or
execute the current mission might potentially be assigned to new
Triggered missions, depending on priorities. The Satisfied tag is used
for mission triggers and for multi-mission priority in the Ops Planner
only.

**Triggered:** A running mission is the only way the Ops Planner
evaluate a mission as a valid candidate for multi-mission units assigned
to it. Therefore, a queued unit that is in a Waiting for Trigger or
Satisfied mission may become assigned to it. The Ops Planner will only
check for dynamic units to be assigned to a mission if it\'s triggered
through the Ops Planner.

The Ops Planner evaluates units assigned to multiple missions for
assignment to the most appropriate Triggered mission, based on the
priority. A unit that is active in a mission in "Satisfied" phase will
still evaluate the satisfied mission and may continue that mission if no
other missions are available.

### 7.5.3 Column Definitions

**Bulk actions**

![](D:/dev_command/Manual/workspace/images/media/image143.png){width="6.3in"
height="0.42430555555555555in"}

Bulk action tools are located on the bottom of the operation planner.
These are used to select multiple mission at once and perform
simultaneous modifications on them.

![](D:/dev_command/Manual/workspace/images/media/image144.png){width="2.4170034995625547in"
height="0.3021259842519685in"}

**Name**

Just like for operation, the mission's name helps for organization.
However, use made Lua scripts might reference a mission by its name, and
it is recommended to be careful when changing mission's name in such
situation.

**Type**

This is the mission sub type as defined in Command's simulation.

**Description**

This is purely an informational tag and does not affect the simulation
at the moment. Use and edit this field to organize yourself.

Generated mission will usually contain some generated information

**Execution Time**

The time, relative to H-Hour at which the mission is estimated to begin.
See **7.5.5 Operation Planner and Lua Scripting** on page
[175](#operation-planner-and-lua-scripting).

**Filter**

The filter tool is used to do a specific term research on mission and
filter the result of this search query.

### 7.5.4 Triggers 

This chapter is the core of the operation planner capabilities. It
allows relationships between mission and a dynamic approach when
executing missions.

A trigger is like a set of a condition and an action, if the condition
is met, then we do an action.

Command evaluates all these triggers every second.

For mission, there are 2 types of actions:

- We start a mission (we set the mission's phase as "Running").

- We finish a mission (we set the mission's phase as "Satisfied").

It is important to understand that Command doesn't have a concept of
mission completion, when tagging a mission as satisfied, command only
indicates that the mission fulfilled enough of its objective to allow
its assigned units to evaluate other mission assignment options. Of
course, all relevant missions have already implicit mission completion
mechanisms, a cargo mission will stop operation once the task is done, a
strike mission won't launch again to strike a non-existent targets etc.

**These 2 actions are tied to a set of conditions.**

**Starting a mission with triggers**

Select any of the mission and look on the right side of the operation
planner window. Notice the main block called "Triggers to Start
Mission", and how it is separated into 3 smaller blocks.

These smaller blocks are individual conditions. Checking them means this
specific condition will be evaluated.

The dropdown on the right of each smaller block is called a conditional
operator.

![Graphical user interface Description automatically
generated](D:/dev_command/Manual/workspace/images/media/image145.png){width="3.2270833333333333in"
height="4.011805555555555in"}As you can see there are 3 types of
triggers that can start a mission:

- A time-based trigger

- A mission dependency trigger

- A Lua script trigger

![Graphical user interface, application, website Description
automatically
generated](D:/dev_command/Manual/workspace/images/media/image146.png){width="3.2395833333333335in"
height="0.7604166666666666in"}**Time-based trigger**

This will be triggered when the scenario date reaches the defined H-Hour
plus or minus a given duration.

![Graphical user interface, website Description automatically
generated](D:/dev_command/Manual/workspace/images/media/image147.png){width="3.2083333333333335in"
height="0.6770833333333334in"}*Example #1: This trigger will be **true**
if we reach H+ 2 hours*

*Example #2: This trigger will be **true** if we reach H- 23 hours*

![Graphical user interface, website Description automatically
generated](D:/dev_command/Manual/workspace/images/media/image148.png){width="3.21875in"
height="0.7291666666666666in"}

**Mission dependency trigger**

This will be triggered if all missions in "missions to check" are in
"Satisfied" phase. In this example, it will be triggered when "Air
Superiority Patrol" mission is in "Satisfied" Phase.

![Une image contenant texte Description générée
automatiquement](D:/dev_command/Manual/workspace/images/media/image149.png){width="3.2083333333333335in"
height="2.3645833333333335in"}

**Lua script trigger**

![Graphical user interface, application Description automatically
generated](D:/dev_command/Manual/workspace/images/media/image150.png){width="3.2191994750656168in"
height="0.729268372703412in"}

This will be triggered if the Lua script contained returns TRUE as a
value. See **5.3 Lua** on page [78](#lua) more information.

**"Finishing" a mission with triggers**![Graphical user interface,
application Description automatically
generated](D:/dev_command/Manual/workspace/images/media/image151.png){width="3.426388888888889in"
height="1.6979166666666667in"}

It was mentioned earlier that Command does not have an explicit concept
of finished mission.

The triggers to tag a mission as "satisfied" work just like the one to
start it.

The first trigger is a time based one, it tracks the elapsed time since
the mission's phase has been set to "Running" and will be true once the
defined time elapsed.

The second one is a Lua script trigger and work identically to the one
in the mission start trigger -- it returns the Boolean value of the
contained Lua script.

**Logical Operators**

![Graphical user interface Description automatically
generated](D:/dev_command/Manual/workspace/images/media/image152.png){width="2.09375in"
height="2.5631944444444446in"}

**Triggers, in Command, are tied with logical operators**.

Take a look at the pictures below. They represent a set of triggers to
start a mission:

We have set all 3 triggers to be checked. On the right of each trigger,
you can notice a dropdown when you can select either the OR or AND
operator. For the triggers to return TRUE and therefore start the
mission (set its phase change to "Running") each checked trigger is
evaluated.

![Une image contenant texte, capture d'écran, tableau de points, argent
Description générée
automatiquement](D:/dev_command/Manual/workspace/images/media/image153.png){width="2.129861111111111in"
height="2.6430555555555557in"}We see in the next example that the first
trigger has "OR" operator, the second "AND" the third "OR." What it
means in this situation is that the second trigger (the one with "AND")
must be true. In addition, the "AND" trigger needing to be true, either
of the first or third "OR" triggers must also be true. If all conditions
are met and the current mission's phase is "On Hold" then the mission
will change it phase to "Running".

![Une image contenant texte, moniteur, capture d'écran, argent
Description générée
automatiquement](D:/dev_command/Manual/workspace/images/media/image154.png){width="2.11875in"
height="2.661111111111111in"}

**Another example:**

**All triggers are checked (and will be evaluated), and each of them
have the "AND" operator.**

**This means that the missions will start when all conditions are
true.**

### 7.5.5 Operation Planner and Lua Scripting

Command has already a powerful Lua scripting framework. The operation
planner allows the integration of your script as a trigger.

Clicking on "Edit Script" in either the "Triggers to Start Mission" or
the "Triggers to Tag Mission as Satisfied" group will bring you to an
interface where you can add your script in.

Just like the rest of the triggers, the Lua Script trigger will be
executed each second for its associated mission. The Lua script must
return a Boolean.

![Une image contenant texte Description générée
automatiquement](D:/dev_command/Manual/workspace/images/media/image155.png){width="4.545833333333333in"
height="4.230555555555555in"}

**Working with estimation**

Command is such a complex simulation that giving an accurate estimation
of an operation duration could take up to hours of computation. The
operation planner provides an instantaneous estimation at the price of
reliability.

The operation planner estimation takes into account all the time-based
triggers and mission dependencies, it simulates a run and then display
the estimated execution tie for each mission.

This estimation works only thanks to the user's input on triggers.

**The special case of Lua script**

You may have noticed that not all triggers are time-based, some depends
on Lua script and cannot be reliably predicted. In this case, you will
have to manually input a value into the trigger in this trigger, shown
on the right.

It is not necessary to check (enable) the trigger, having an unchecked
"Time Elapsed" trigger with a value basically tells the operation
planner: "Only use this trigger when estimating execution time". In this
example, we assume the mission will be satisfied after 1 hour.

![Graphical user interface, application, website Description
automatically
generated](D:/dev_command/Manual/workspace/images/media/image156.png){width="3.2291666666666665in"
height="0.59375in"}

If everything is properly configured, clicking on the "Simulate" button
will calculate the execution time, relative to H-Hour for each mission.

![Une image contenant texte, capture d'écran, moniteur, argent
Description générée
automatiquement](D:/dev_command/Manual/workspace/images/media/image157.png){width="6.3in"
height="3.995833333333333in"}

## 7.6 Air Tasking Order

![](D:/dev_command/Manual/workspace/images/media/image158.png){width="6.322916666666667in"
height="2.634549431321085in"}

The purpose of the air tasking order (ATO) is to enable the control of
multiple air forces in one operational environment. At the most basic
level, it provides an overview of all the air sorties as well as the
appropriate status, missions used and various timings as appropriate.

The show flights option at the top of the screen enables you to filter
and show the flights that you are more interested in during a given
scenario. The show airborne and show planned flight plans option gives
you the ability to see the flight plan and make changes to of it of the
currently selected flight. Note that after selecting any flight, it is
possible to click the edit flight plan button at the base of the screen
to make direct edits to the flight plan of that group.

The create, copy and delete flights allow you to modify any flight that
you have highlighted in the ATO. Creating a blank flight allows you to
pre-plan all aspects of a flight without having a set mission in place.
You can even design a flight plan and then select Change a/c type and
loadout for the purposes of pre-selecting the appropriate aircraft from
an existing aircraft that you possess in the scenario already.

It is also possible to change the type of flight plan to a flight plan
template. This template can be used to create a standard model with all
the appropriate settings built in that can later be applied to other
units and missions at a later time. The best use of the ATO is to
monitor what a large quantity of aircraft are doing at any given time,
and to be able to quickly find everything you need to know about the
various missions throughout a scenario.

## 7.7 Mission/Operations Lua Reference

**[Mission Lua Wrapper]{.underline}**

**PriorityWeight** (Read/Write) \[int\]

How important this mission is (0 = most important) affects multi-mission
units\' assignment dynamic.

**OperationName** (Read/Write) \[string\]

Used to organize mission into groups, it is an informational element
shown on the operation planner UI.

**Completion** (Read/Write) \[float\]

From 0.0 to 1.0, it designates how complete this mission is. This value
is mostly unused in most cases at the moment and should be ignored.

**Phase** (Read/Write) \[ENUM\]

The phase as interpreted by the operation planner, this rules the whole
dynamic in the operation planner and the assignment of multi-mission
units.

MissionPhase ENUM:

None = 999

Auto = 0

Completed = 10

Active = 20

OnHold = 30

**MISSION START BY TIME TRIGGER**

**MissionStartTrigger_Time** (Read/Write) \[int\]

The H +/- time condition for the trigger.

**MissionStartTrigger_Time_Enabled** (Read/Write) \[Bool\]

Is the trigger used or not?

**MissionStartTrigger_Time_LastResult** (Read) \[Bool\]

What was the last result of the trigger the last time it has been
evaluated?

**MissionStartTrigger_Time_Operator** (Read/Write) \[Bool\]

The trigger\'s operator. True = \'AND\', False = \'OR\'

**MISSION START BY MISSION COMPLETED**

**MissionStartTrigger_MissionCompleted** (Read/Write) \[NLua.LuaTable\]

The condition for the trigger, defined as all the missions that need to
be completed (phase as \"satisfied\") for the trigger to check.

*Example :*

*\>\> local mission = ScenEdit_GetMission(\'USA\',\'Shore A LCAC 1 #4
Wave 1\')*

*print(mission.MissionStartTrigger_MissionCompleted)*

*mission.MissionStartTrigger_MissionCompleted =
{\"LTACBA-0HMBO9DVSMOPI\",\"LTACBA-0HMBO9DVSMOP9\",\"LTACBA-0HMBO9DVSMOPB\"}*

*print(mission.MissionStartTrigger_MissionCompleted)*

*{ \[1\] = \'LTACBA-0HMBO9DVSMOPI\' }*

*{ \[1\] = \'LTACBA-0HMBO9DVSMOPI\', \[2\] = \'LTACBA-0HMBO9DVSMOP9\',
\[3\] = \'LTACBA-0HMBO9DVSMOPB\' }*

**MissionStartTrigger_MissionCompleted_Enabled** (Read/Write) \[Bool\]

Is the trigger used or not?

**MissionStartTrigger_MissionCompleted_LastResult** (Read) \[Bool\]

What was the last result of the trigger the last time it has been
evaluated?

**MissionStartTrigger_MissionCompleted_Operator** (Read/Write) \[Bool\]

The trigger\'s operator. True = \'AND\', False = \'OR\'

**MISSION START BY LUA CONDITION**

**MissionStartTrigger_LUADescription** (Read/Write) \[String\]

The label of the lua script as an indicator of its purpose.

**MissionStartTrigger_LUA** (Read/Write) \[String\]

The lua script to be executed for this trigger conditions, must return a
Boolean as a condition result.

**MissionStartTrigger_LUA_Enabled** (Read/Write) \[Bool\]

Is the trigger used or not?

**MissionStartTrigger_LUA_LastResult** (Read) \[Bool\]

What was the last result of the trigger the last time it has been
evaluated?

**MissionStartTrigger_LUA_Operator** (Read/Write) \[Bool\]

The trigger\'s operator. True = \'AND\', False = \'OR\'

**MISSION COMPLETED (\"SATISFIED\") BY ELAPSED TIME OF MISSION
EXECUTION**

**MissionCompletedTrigger_ElapsedTime** (Read/Write) \[int\]

The elapsed time since mission execution for the trigger\'s condition to
return true.

**MissionCompletedTrigger_ElapsedTime_Current** (Read/Write) \[int\]

The current elapsed time.

**MissionCompletedTrigger_ElapsedTime_Enabled** (Read/Write) \[Bool\]

Is the trigger used or not?

**MissionCompletedTrigger_ElapsedTime_LastResult** (Read) \[Bool\]

What was the last result of the trigger the last time it has been
evaluated?

**MissionCompletedTrigger_ElapsedTime_Operator** (Read/Write) \[Bool\]

The trigger\'s operator. True = \'AND\', False = \'OR\'

**MISSION COMPLETED (\"SATISFIED\") BY LUA CONDITION**

**MissionCompletedTrigger_LUADescription** (Read/Write) \[String\]

The label of the lua script as an indicator of its purpose.

**MissionCompletedTrigger_LUA** (Read/Write) \[String\]

The lua script to be executed for this trigger conditions, must return a
Boolean as a condition result.

**MissionCompletedTrigger_LUA_Enabled** (Read/Write) \[Bool\]

Is the trigger used or not?

**MissionCompletedTrigger_LUA_LastResult** (Read) \[Bool\]

What was the last result of the trigger the last time it has been
evaluated?

**MissionCompletedTrigger_LUA_Operator** (Read/Write) \[Bool\]

The trigger\'s operator. True = \'AND\', False = \'OR\'

**Operation Lua Wrapper**

The 'Operation' object can be fetched from the side object. There is
only one operation object per side.

**LHourMission** (Read/Write) \[LuaWrapper_Mission\]

The mission designated to start at L-Hour. As soon as the L-Hour is
reached, the mission will change phase to "Running".

**HHourMission** (Read/Write) \[LuaWrapper_Mission\]

The mission designated to start at H-Hour. As soon as the H-Hour is
reached, the mission will change phase to "Running".

**HHour** (Read/Write) \[String\]

The time set as H-Hour.

**LHour** (Read/Write) \[String\]

The time set as L-Hour.

**HHourEffectiveStartTime** (Read/Write) \[String\]

The effective time at which the H-Hour started counting. Sometimes the
actual H-Hour can be different from the one planned initially, or in the
past.

**LHourEffectiveStartTime** (Read/Write) \[String\]

The effective time at which the L-Hour started counting. Sometimes the
actual L-Hour can be different from the one planned initially, or in the
past.

**H_LHourAreRelative** (Read/Write) \[String\]

Whether or not the H-Hour and the L-Hour have a static time delta. With
this option on TRUE, the H-hour and L-hour will always have the same
time difference and will adjust automatically when changing either the
H-Hour or the L-Hour

**Unit Lua Wrapper**

**AllowMultiMission** (Read/Write) \[Bool\]

Is the mission allowed to have multiple missions assigned to it and will
it be considered by the operation planner logic?

**AssignedMissionsQueue** (Read/Write) \[NLua.LuaTable\]

The list of missions assigned to this unit. This is the missions the
operation planner evaluates every tick.

## 7.8 Pier and other operations 

Ships & submarines have the ability to dock with designated parent ships
and facilities and be serviced while docked.

### 7.8.1 Placing and using piers

Pier facilities extend passable "pier lane" areas around them that allow
ships to navigate to pier areas even slightly inland (similar to
canals). This allows true-to-life positioning of pier facilities without
having to flatten the terrain data around them in order to make them
accessible.

![Pier3](D:/dev_command/Manual/workspace/images/media/image159.png){width="6.138888888888889in"
height="3.1527777777777777in"}

The light-shadow polygon is the "pier lane" area projected by the
multiple pier facilities inland. Ships and submarines can freely
traverse this area (even though terrain is nominally present) to
navigate in and out of the piers.

Once a ship docks to a pier (or parent ship), the process of refuel,
repair and replenishment begins. Both refueling and rearming happen at
faster rates than on UNREP hookups as the docking condition allows for a
stabler environment and more extended facilities and tooling. In
addition, while a ship underway can perform repairs only to minor
component damage and cannot repair structural damage, docked units can
perform repairs on medium- and heavily-damaged systems, and can also
repair their structures. Docked ships/subs can re-arm from either
magazines on the pier itself or ammo facilities belonging to the same
group (i.e. naval base) as the pier, just like with ammo bunkers on
airbases.

Pier side replenishment rates are modeled after real-life restrictions
on size & weight. Light weapons can be loaded quite fast, but heavier
weapons (particularly heavy gun shells or large bombs, missiles or
rockets) can take hours to transfer and load.

Readying a ship for redeployment differs from aircraft turnaround in a
number of ways. Ship preparation typically takes far longer than
aircraft (except for very small boats), and in contrast to an aircraft,
a ship is perfectly able to put to sea again while still in far from
optimal condition. Accordingly, the player can order one or more ships
to redeploy while they still have damage or miss weapons and fuel.

To enable the AI to make reasonable decisions on withdrawal &
redeployment thresholds, a dedicated set of doctrine settings are
available: Withdraw & Redeploy criteria.

![Pier1](D:/dev_command/Manual/workspace/images/media/image160.png){width="6.180555555555555in"
height="4.027777777777778in"}

The status of each of those aspects is continuously tracked and
evaluated against the doctrine threshold and a ship will withdraw from
its mission if any of the withdrawal criteria are reached. Conversely,
while docked, these criteria are regularly checked, and a ship is
allowed (by the AI) to re-sortie only if everything is "green across the
board". The player of course can still order any ship to sail
immediately regardless of its condition.

These new settings allow tailoring the withdraw and redeploy behavior of
a ship to its unique strengths / weaknesses as well as to the needs of
her mission tasking. For example, an anti-aircraft escort may be set to
ignore depletion of its offensive weapons, fuel and any damages to
itself and withdraw from the line only when its defensive (AAW) armament
is depleted. Conversely, a sensitive high-value unit may be configured
to withdraw immediately on the first scratch of damage.

> ![Pier2](D:/dev_command/Manual/workspace/images/media/image161.png){width="6.152777777777778in"
> height="1.6944444444444444in"}

The redeployment criteria allow the player (or scenario author) to make
his own decisions on how "ready" he wants his ships to put out to sea
again: Does he wait until every last bit of ammo is restocked? Is it
enough to repair damage and get refueled? Obviously, there is no single
"best" answer, and the theater/operational exigencies (as well as time
pressure) are likely to force the player to make decisions that he is
not entirely happy with. Real-life ops are very often a compromise, and
Command reflects this.

When putting out from a pier to sea again, ships/subs first navigate to
a point at the edges of the pier lane area and then re-plot for their
destination.

*[NOTE #1: The definition of primary attack/defense weapon points to the
longest-ranged ASuW weapon (attack) and AAW/ASW (defense) weapon and
uses the default DB-fed values for reference. So, for example, if an
Aegis cruiser is stocked with SM-2s on its DB-pristine version but the
scenario author opts to clean them out and re-stock with TLAMs and a few
ESSMs, the cruiser is considered as "primary defense weapon exhausted"
even though it still has the ESSMs.]{.mark}*

*[NOTE #2: The rules for picking the primary attack/defense weapon are
slightly different for submarines. Hunter-killer subs (both nuclear and
DE) consider torpedoes their primary weapon for both attack and defense
even if they carry other longer-ranged weapons (missiles etc.). Cruise-
and ballistic-missile subs however, consider their missiles their
primary attack weapon.]{.mark}*

### 7.8.2 Observing (and cataloging) non-friendly air/docking ops

Aircraft, ships and submarines can be spotted on their host facilities
during a BDA/recon attempt by a friendly unit. There are two ways of
spotting hosted units:

1\) When a unit with a visual/IR/radar sensor performs BDA on a naval or
air base, it also performs recon on its open-air air (revetments,
parking areas, pads, runways etc.) or docking (piers, docks, drydocks
etc.) facilities respectively.

2\) Assets under cover are not completely safe from observation either:
If an aircraft enters or exits an enclosed air facility (e.g. a fighter
that has just landed is entering a hangar to re-ready) **while a unit is
observing this facility**, the aircraft is also spotted (the same holds
for e.g. a submarine entering an underground base). This means that
"persistent" recon/intel assets (anything from a SOF team parked outside
the base, to a stealthy RQ-170/180 loitering overhead or even a
satellite perched far up in HEO/GEO orbit) are essential for keeping
track of under-roof traffic and inventory.

Units spotted either way are kept on record and classified/identified as
per the normal detection/classification rules. This is also reported on
the message log. A "spotted hosted unit" record also contains age info
so that the player is aware how stale this spotting report is *(a "5
mins ago" observation obviously holds different value than a "2 weeks
ago" one)*.

On the map, friendly facilities that host units AND contacts on which
hosted units have been spotted are displayed with a "black triangle on
yellow box" symbol. This allows at-a-glance awareness of which friendly
assets (and contacts) host units:

If a unit gets close enough for a re-recon of a contact with spotted
hosted units, the existing spot records are re-evaluated and refreshed,
and any now-missing units are discarded from the recon reports.

Spotted unit records are listed on the "Contact Report" window, on a new
"Hosted units spotted" tab:

> ![Recon3](D:/dev_command/Manual/workspace/images/media/image162.png){width="4.361111111111111in"
> height="2.5416666666666665in"}

### 7.8.3 Underway Replenishment (UNREP) and other logistics

The rate at which a given store can be transferred to the receiver unit
is determined by the characteristics of the item:

- Guided weapons up to 10kg, gun & rocket rounds up to 15mm: One per
  second.

- Guided weapons up to 50kg, gun & rocket rounds up to 24mm: One per 5
  seconds.

- Guided weapons up to 100kg, gun & rocket rounds up to 60mm: One per 15
  seconds.

- Guided weapons up to 150kg, gun & rocket rounds up to 80mm: One per 30
  seconds.

- Guided weapons up to 250kg, gun & rocket rounds up to 150mm: One per
  minute.

- Guided weapons up to 500kg, gun & rocket rounds up to 200mm, depth
  charges, mines, decoys, dispensers, drop tanks, laser charges and
  everything else not covered: One per 5 minutes.

- Guided weapons up to 1000kg, gun & rocket rounds up to 350mm: One per
  15 minutes.

- Guided weapons up to 2500kg, gun & rocket rounds up to 450mm: One per
  30 minutes.

- Guided weapons heavier than 2500kg, gun & rocket rounds larger than
  450mm: One per hour.

The rate is further affected by the UNREP capability of the receiving
unit, doubled if the provider is a land facility (stability and more
equipment), and halved if the receiver is a submarine (more complicated
to get anything bulky inside a sub).

![A screenshot of a computer program Description automatically
generated](D:/dev_command/Manual/workspace/images/media/image163.png){width="5.0in"
height="2.0625in"}

The scenario button allows you to choose what scenario you would like to
benchmark and can be selected from any saved scenarios in the
appropriate folder.

**Iterations --** Allows you to select how many runs through the entire
scenario that the benchmark mode will execute.

**Fidelity --** This allows you to select how precise the
moment-by-moment calculations should be completed. In scenarios where
there are very large numbers of units, selecting a high fidelity will
result in significantly longer run times.

While running, the benchmark mode will indicate what the current
scenario time is, and it will show you how long each 'pulse' is taking
to execute. A shorter pulse time indicates a faster running scenario.
Note that when the benchmark is running, if there is no mission
termination or units on any of kind of mission, the benchmark mode will
run very quickly but nothing will actually be going on in the scenario
giving bad results.

When the benchmark is complete, you will receive a report on the
different lengths of pulse times as well as the highest level of time
acceleration achieved. You can press the abort key at any time if you
need to stop the process.

#  
