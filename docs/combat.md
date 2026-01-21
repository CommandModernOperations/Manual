# 9.0 COMBAT

Combat in Command involves several basic factors. First one must see the
opponent. Then you must hit the opponent. The former involves sensors,
the latter involves weapons.

## 9.1 Sensors

COMMAND has several different types of sensors that can be divided into
four main categories: radar, ESM, sonar, and optical sensors. All
sensors have a physical height associated with each of the components.
You often see radars mounted on tall towers or on the tops of the masts
of ships, this is done to improve the sensors visibility of the horizon.
The mast height of a given unit can be explicitly set by the unit
designer, or it will be estimated based on the overall size of the
platform.

### 9.1.1 Radar 

Radar functions by sending radio waves at the target. COMMAND contains
radars from the earliest and crudest sets to extremely advanced
electronic arrays. As radars are active, they all have an inherent risk
of being jammed and giving their whereabouts away. However, a more
advanced radar will be less vulnerable to this, especially if faced
against a less advanced jammer.

Radars have a limited field of view they can search and track their
targets within. Fire control radars in particular often have very small
beamwidths of a few degrees that can only concentrate their emissions in
a limited sector of the sky. Complicating this equation is how
mechanically steered radar beams require a non-zero amount of time to
orient themselves to a certain direction. Because of this, long range
radars require several seconds to complete a circular sweep, and many
early aircraft radars had very limited fields of view for search
purposes. In COMMAND, this effect is modelled in several ways, and
understanding the limitations often creates new tactical opportunities.

Once a mechanically steered radar wishes to hold its beam on a certain
target, it can no longer 'turn' to face another target. If the radar is
an illumination type radar, it has to have a continuous line of sight on
that target at the cost of not being able to engage other targets. In
addition, all radars have vertical and horizontal limits based on the
generation and type of radar. These limits provide unique options for
avoiding the beam of the radar by simply staying out its effective field
of view. This also means that approaching a SAM battery, for example,
from multiple directions simultaneously prevents the SAM from reliably
engaging in all directions. Note that depending on the generation of the
radar, the ability to detect targets that are 'below' the radar and are
close to ground clutter may be limited.

Compare several American fighter radars:

AN/APQ-120 (F-4): Basic mechanical scan radar. The earliest and least
capable. With no "track while scan" function, it can either guide
missiles to its painted target *or* search for contacts, but not both at
the same time.

AN/APG-63 (F-15A): Mechanical scanning, frequency agile. Frequency agile
radars are less susceptible to jamming and "doppler notching", an air
combat technique where an aircraft flies perpendicular to the emitter.

AN/APG-70 (F-15C): Mechanical scanning, frequency agile, NCTR-JEM. In
addition to move advanced electronics, an F-15C with this radar will
have the ability to identify enemy aircraft flying head-on, as its NCTR
radar "counts" the fan blades of their engines.

AN/APG-77 (F-22): Active electronically scanned array, NCTR-NBILST. This
incredibly advanced radar is electronically scanned, making gimmicks
like doppler notching pointless. Its NBILST (Narrow Beam Interlocking
Search and Track) NCTR function means it can positively identify aerial
targets from any angle. Phased array radars also do not have the issues
with scanning up and down that less sophisticated models do.

Electronically scanned arrays have other benefits besides having
enhanced detection capabilities. They are better able to filter out
jamming thanks to their frequency agility and more importantly, they are
more resistant to ground clutter once a target has been initially
located. Ground clutter can still affect their search modes as in
conventional radar, however in tracking modes, the electronic array
radars are very precise, efficient and difficult to force a broken lock.
One of the downsides of an electronically scanned array radar is that
the strongest detection capability comes from the center of the radar
projecting perpendicular to the face of the array. This means that
forces wishing to be undetected can avoid being in the center lobe of
the radar, and have enjoy a significantly reduced chance of detection
when compared to conventional pulse-based radar.

### 9.1.2 ESM

Electronic Support Measures are passive systems that can detect
electronic emissions (radar, OECM jammers). They range from simple,
crude radar warning receivers that can give a vague and imprecise (yet
still very important) notification that an emitter is somewhere nearby
to advanced detectors, that, based on the electronic sources, can
conclude that the emitting platform is a MiG-29 Fulcrum A with a N-019EB
radar. In COMMAND, aircraft will now start defensive maneuvering the
moment that they detect illumination by a fire control radar, even
before a missile is detected on route to the aircraft.

ESM platforms, even more precise ones, have an inherent lack of
precision compared with active sensors that constantly "paint" the
target. However, having multiple ESM-equipped units present can counter
that to a large extent by triangulating the signals.

### 9.1.3 Optical Sensors

Almost every human has two optical sensors in the front of
their head. In addition to the "Mk 1 Eyeballs", COMMAND boasts many
types of *electro-*optical sensors, including cameras and infrared
systems. These range from early, cumbersome TV cameras to incredibly
sophisticated imaging infrared systems.

The biggest advantage optical systems offer over radars is their
passivity. Because optical systems are considered "passive" sensors and
do not emit, they are not vulnerable to being picked up by ESM the way
radars are. Imaging optical systems also can confirm the identity of a
target in a way that most radars cannot.

However, optical systems also have significant disadvantages. One is a
"looking through a straw" effect where the camera has a very limited
field of view. Another is a lack of precision, with electro-optical
systems working by themselves can only gain precise target information
at very short ranges.

### 9.1.4 Sonar

Active sonar is like underwater "radar" (an apt comparison, as both
reflect waves of energy off the target). It creates a more precise
contact at the expense of being easily detected. Passive sonar has many
of the same weaknesses as electro-optical systems (imprecise, especially
at long range) but also their strengths (passive, does not give away the
sensor when being used). Vertical flank arrays are now used to create
more precise target tracks against underwater targets.

Towed arrays are used on many ships and submarines. They can be held a
distance away, making them less vulnerable to their own engine noises,
and they can sit below the thermal layer, reaching past it the way a
hull sonar on a surface ship cannot.

### 9.1.5 PCLS

One newer type of electronic detection is the passive coherent location
system (PCLS). This system uses the reflection of electronic waves
against the body of an object but instead of utilizing a
transmitter/receiver combination as in conventional radar, it uses
existing electromagnetic noise created by everything from cell phone
towers to VOR beacons. The PCLS monitors the propagation and properties
of these existing signals with multiple receivers spread apart to
determine the presence of an object without having an active signal of
their own. In order for this process to work, there has to be an
appropriate set of transmitters as well as a constellation of typically
ground based receivers.

In COMMAND, PCL systems are modelled by placing several sources of
electromagnetic emission such as radio and tv towers and the setting up
a PCL platform in a position where it can receive both the 'echoes' of
the target as well as the source of the radiating signal. It typically
takes three or more accurate sources and reflection to develop a strong
enough track and while PCL can determine the vicinity of the target, a
targeting quality track will require alternate detection systems to
acquire that target. PCL is therefore an excellent and passive early
warning system, but upon detection, traditional sensors are required for
a quality track.

### 9.1.6 MAD

Magnetic Anomaly Detectors are used by anti-submarine aircraft. They
search by measuring magnetism and looking for large anomalous deposits
of metal (i.e. submarines) under the water. Thus, the ideal MAD subject
is a large submarine (lots of that metal!) in deep water (less
background metal to get in the way)

While passive, MADs are ***not precision sensors.*** They do not have a
range component and only have a vague bearing element-this is why
maritime patrol aircraft still carry all the sonobuoys that they do.

## 9.2 Weapons

### 9.2.1 Unguided Weapons

Unguided weapons include guns, bombs, and rockets. Their accuracy is
determinant on many factors, including the skill of the operator, the
type of fire control system, and the range to the target.

Ballistic missiles represent one class of unguided weapons and have
unique properties in the way that they are deployed, travel and operate.
Most ballistic missiles operate by having a large rocket power a payload
into a tall parabolic arc. When the rocket burns out, the weapon
continues to glide to its apogee before gravity and drag catch up and
the weapon begins to glide back towards the ground. In some ballistic
missiles, particularly ICBMs, the payload of the weapon detaches from
the main body of the weapon and as such presents a much smaller and more
difficult target to destroy. In addition to the payload containing a
warhead, ballistic missiles may now be equipped with decoys or
hypersonic glide vehicles (HGVs) to increase the probability of striking
the target and not being intercepted.

COMMAND models all phases of a ballistic missile trajectory in detail
and the challenge in detecting and successfully intercepting these
weapons. Although many countries throughout the world have developed
dedicated systems to defeat these weapons, the incredibly high speeds
and the enhanced maneuverability of recent systems has resulted in
several countries seeking systems other than guided missiles, including
sci-fi like lasers and high-velocity weapons. COMMAND models all phases
of ABM carefully and dedicated systems for the purposes of shooting down
ballistic missiles fire when the proper opportunity is detected.

### 9.2.2 Guided Weapons

Guided weapons include guided missiles and so-called "smart bombs". The
guidance systems present in COMMAND include:

- Inertial guidance. The weapon is programmed to fire on a specific set
  of coordinates and its internal systems direct it (to the best of
  their ability) to those coordinates. Weapons with inertial guidance
  range from early ballistic missiles that will be lucky to land in the
  boundaries of their target city to advanced, ultra-precise weapons.

- Optical guidance. The weapon homes in on an image of the target.
  Optical systems range from early, crude ones like the GBU-8 HOBOS to
  advanced imaging infrared systems (that can even act as makeshift
  sensors in their own right).

- Infrared Guidance. The weapon homes in on the heat signature of the
  target. In modern seekers with imaging systems this overlaps with
  "optical guidance", but it applies also to early heat-seeking
  missiles. Anti-air IR missiles come in three varieties:

  - Stern chase (need to be right behind to get a good lock, i.e.
    AIM-9b/AA-2),

  - Rear Aspect (still need to be behind; yet are more flexible than
    stern-chase weapons, IE, AIM-9H/AA-8)

  - All Aspect (can fire on the target from any angle, i.e.
    AIM-9L+/AA-11).

- Semi-Active Radar Guidance: In short, this guidance system involves
  the missile homing on a target "painted" by a radar. Breaking the lock
  (such as forcing the launcher to turn away) will cause it to lose
  control.

- Semi-Active Laser Guidance: This is the classic laser guided bomb,
  where the launcher paints the target with a laser designator and the
  weapon homes in on the designator. Some types of weapons can use
  "buddy lasing" (where an aircraft or even a ground unit can designate
  the target while the other drops from farther away)

- Active Radar Homing: This involves an emitting radar system on the
  weapon itself. ARH was pioneered on anti-ship missiles like the SS-N-2
  that were big and only had to engage slow targets. Later it became
  miniaturized enough to be used for AAW weapons like the AMRAAM.

It's important to note that ARH does not necessarily mean the weapon can
just be fired "blindly". Most AMRAAM-style ARH air-to-air weapons
(except for newer ones with an appropriate datalink and a friendly
illuminator nearby, like an E-2D Advanced Hawkeye and AIM-120D advanced
AMRAAM) need the launching platform to detect and illuminate the target
with its own radar before launching.

Guided missiles have an additional challenge to employment, and that is
in how they propelled towards the target. While the popular view of
missiles in movies depicts a slow-moving projectile powered continuously
throughout flight, only cruise missiles have that type of capability.
The majority of missiles use a boost-coast model for propulsion meaning
that they burn their motors for a certain amount of time to build up
speed and then glide towards the target using the energy they
accumulated during their initial acceleration. Not only does this mean
that a typical guided weapon operates at its peak speed for only a few
moments before atmospheric drag and gravity takes over, slowing the
weapon down. This tendency for a missile to exhaust itself in thicker
air along with losing energy as it maneuvers is one of the defenses a
modern pilot has against these formidable weapons.

It is also worth noting that some guided weapons, particularly those
optimized for very long-range engagements, employ not only a boost-glide
model, but utilize a very high lofted trajectory whereby the guided
weapon is shot to very high altitudes where atmospheric drag is less and
then glides downwards onto the target constantly accelerating due to the
force of gravity. Many of these types of guided weapons are 'smart' in
that they will select the optimum trajectory depending on the
interception time and range to the target.

There are some guided weapons modelled in command such as the RIM-174
(SM-6) that use a continuous burning motor. These types of weapons are
usually employed against ballistic missiles or very high-altitude
targets and will also include maneuvering jets to improve interception
accuracy in exoatmospheric engagements.

COMMAND also models loiter-type weapons such as the ALARM anti-radiation
missile. This weapon is designed in such a way that if it loses contact
with an emitting target, it deploys a parachute and begins gliding
downwards. When the target radar system is reacquired, the parachute is
jettisoned and the rocket motor fires again providing the required
thrust to complete the weapon's journey towards the target.

Some guided weapons have multiple types of guidance built into them.
This provides an additional layer of redundancy should one of the
seekers or fail or the target is impossible to detect using it. An
example of one of these weapons is the AIM-88E AARGM, a specialized
radar-destroying missile that can use passive radar guidance to home
into a radar but in the event that the radar is turned off, it can use a
combination of GPS and active radar to guide towards the target.

### 9.2.3 Torpedoes

Torpedoes swim through the water. There are two main guidance systems in
the initial torpedo phase:

-Inertially guided torpedoes are the earliest types of torpedoes in
COMMAND. An example is the classic Mk14 World War II torpedo. They have
no way of changing course once fired.

-Wire guided torpedoes are connected to their parent submarines and can
be steered as if they were units in their own right via the Plot Course
function while the wire is active (one use of this is to prevent the
torpedoes from piling up on one target).

However, turning extremely fast (as in, "the sub's life is in danger"
fast) or just moving quickly (over ten knots) while firing the torpedoes
will likely cause the wires to break. A torpedo with a broken guidance
wire goes autonomous, activating its terminal seeker and going out of
the launcher's control.

-Torpedo terminal guidance includes traditional sonar guidance and
wake-homing. The former is considerably easier to decoy.

### 9.2.4 Lasers

-Since the first pulp hero obliterated the first space monster with a
ray gun, people have dreamed of turning fiction into fact. Now, after
decades of development and the successful use of military lasers for
targeting purposes, the dream is finally becoming a reality. Lasers are
modeled in COMMAND.

-Lasers come in four categories, each with their own characteristics.
Chemical Oxygen Iodine (COIL), Deuterium Fluoride, Carbon Dioxide, and
Solid State/Fiber. COIL and DF lasers use chemical feeds as "ammunition"
and are thus exhausted and reloaded like conventional weapons, while CO2
and SS/F lasers draw on their parent's power plants and can keep firing
as long as it lasts.

-As they move at the speed of light, lasers attack their target
instantly, giving it no evasion bonus. However, they can only
immediately destroy the smallest targets, requiring sustained exposure
for larger ones. Turning on the "Aircraft Damage" setting is thus highly
recommended for scenarios that involve lasers.

**HVPs/railguns:**

The High Velocity Projectiles currently in COMMAND are modeled similarly
to missiles, only fired from certain guns. They are treated as "guided
weapons" in the database and offer their users plentiful, long-range,
accurate strike capability.

### 9.2.5 Electromagnetic Pulse (EMP)

Electro-magnetic pulses serve to destroy electronics. The effects they
have on their targets depend on the intensity of the pulse (which is
*not* affected by the warhead's yield in the classic "nuclear EMP"
scenario but is affected strongly by its detonation altitude), the
operating status of the target (active sensors are more vulnerable) and
the technology generation (older -think vacuum tube-) electronics are
the most resistant, while increasingly advanced ones become increasingly
more susceptible).

EMPs can be unleashed in multiple different ways.

- As the byproduct of a nuclear warhead used for other purposes.

- By a Lua-induced "Add Explosion" action, particularly detonated at an
  extremely high altitude for maximum effect.

- By a "one-click EMP" attack. Take a suitable weapon, manually allocate
  it, and in the upper right "weapons allocated window", right click on
  the weapon record and select "Special high-altitude detonation". It
  will then detonate at the optimum altitude for an EMP wave.

- By a weapon with a non-nuclear "tactical EMP" warhead.

EMP warheads come in two main types: directed and omnidirectional.
Omnidirectional or O-EMP can be compared to a hand grenade in how once
it detonates, it creates a blast that affects all electronics in
spherical radius emanating from the blast point. Directional or D-EMP
weapons are designed to focus the effects of the EMP burst on a small
target. O-EMP is effective at causing less damage but to more targets
whereas D-EMP is better at disabling a specific system through
concentration of the effect.

### 9.2.6 Warhead Types

Warheads can come in various types, from conventional explosives to area
ones like airbursts, napalm and clusters (little penetration but a
"smothering" effect and lots of flames/secondary damage) to specially
designed penetrators (those that can "punch above their weight" by
breaking through deeply). As in real life, damage in COMMAND can
manifest in strange ways.

### 9.2.7 Decoys

Decoys are units completely identical to the "real" ones but with a
Decoy flag set to true. In the real world a decoy can move or not, be
armed or not. In order to achieve maximum flexibility a decoy is created
as an exact copy of the mimicking unit with the only exception of a flag
that indicates this as a decoy.

The scenario editor can freely customize the unit removing weapons or
propulsions until it reaches the desired level of simulation.

![A screenshot of a computer Description automatically generated with
medium
confidence](images/image165.png)

The side that owns the unit will always be able to see that the unit is
a decoy thanks to the tag in the right column.

Decoy identification:

![A screenshot of a computer Description automatically
generated](images/image166.png)

The simulation will make no effort in auto-identify a decoy. It will be
the player that once identified a unit as a decoy can right click on it
and mark it as decoy. The specific defending unit holds a list of side
ID that have been marked it as a decoy. Once the unit is marked as a
decoy (independently of the fact that the unit is indeed a decoy) the
unit is always treated as a waste of ammo and no attempt at auto engage
is made, although manual fire will still be possible.

The unit marked as decoy will change its icons with the decoy icon
already in the symbol folder and will have the Decoy tag in the right
column when inspected. A unit can be unmarked as decoy by right clicking
on it and select again "toggle decoy". This will revert the unit to be
considered as a real unit of the identified type

## 9.3 Battle

In the combat itself, there are several "steps" gone through before the
combat is resolved. The first step is identification. Targets (for
attackers) and threats (for defenders) have to be resolved in a process
that takes time depending on the unit's proficiency and OODA clock (see
**6.3.4 Database Viewer** on page [116](#database-viewer)). The next
step is actually engaging, where the unit moves in range and fires its
weapons. This may sound simple, but in execution, it's anything but.

### 9.3.1 Air Combat

An air unit's ability to engage is dependent on more than just pure
range. It also depends on sensors and/or the capability of the weapon.
So, at one extreme, there are early stern-chase infrared missiles that
require the attacker to line up straight behind the target and early
SARH missiles that render the attacker's radar unable to do anything
else while it guides them. At the other are all-aspect, off-boresight
missiles; able to be launched from incredible positions with a helmet
mounted sight and CEC-datalinked active radar missiles able to be
launched from far away and guided by another aircraft with the launcher
never needing to turn on its position-exposing radar.

The target may not see anything and only hope the aiming of the guns is
poor or the missile prone to inaccuracy (This is historically accurate,
as the overwhelming majority of losers in air combat never saw anything
until it was too late). Should they notice, the target shifts to
"engaged defensive" and attempts countermeasures. These countermeasures
include dodging, countermeasures, and aggressive maneuvering.

Dodging, trying to "beam" (fly perpendicular to) the weapon or radar.
This results in a dice roll that gives it a penalty to hit. The penalty
is highly dependent on the target's skill and aircraft agility. Even a
master pilot can't do much in a lumbering cargo plane or heavy bomber,
but in a nimble fighter, a novice can lose a dogfight to a plane of an
earlier period. Dodging does not apply just to missiles. The enemy
aircraft itself or the radar can trigger evasion, the latter to attempt
"doppler-notching", a way of exploiting limitations of (particularly
earlier) radars. Aircraft maneuvering in dogfights is affected by
physics, which range from airframe limitations (aircraft have to roll
into turns) to pilot limitations (as seen on the right-hand display
under G-force).

Deploying countermeasures, such as chaff and DECM against radar guided
missiles or flares/IRCM against infrared ones. This is highly dependent
on the technology level of both weapon and countermeasure and is treated
as a separate calculation before the dodge phase.

Example: A shah-vintage Iranian F-4 Phantom engages a modern, highly
skilled American fighter over the Strait of Hormuz with ancient early
AIM-7s. While a victory is still possible, it's a steep hill to climb.
Even before the skill of the American pilot and the weaker kinematics of
the Sparrow come into effect, the missile must overcome a chaff release
and electronic jammer, both of which it is highly susceptible to. When
the situation is reversed, the old electronics and chaff of a Phantom or
even Tomcat offer far less in the way of protection against an AMRAAM.
If the target survives or notices the attack before it hits and has an
appropriate weapon, they may be able to maneuver and fire back. Then the
situation repeats itself.

Other aircraft are not the only danger that modern aircraft face, and
thanks to improved missile and radar designs, surface-to-air missile
batteries have evolved significantly and their efficiency and
effectiveness against flying targets cannot be understated. These
systems are able to able to launch missiles that routinely travel at
several times the speed of sound with enough accuracy to strike
ballistic missiles from hundreds of miles away.

Once an aircraft is fired upon by a SAM, it has several options at its
disposal in order to reduce the probability of being struck by the
weapon. The first maneuver it to simply turn the aircraft around and run
at maximum speed away from the weapon. Since most SAMs use a boost-glide
method to get to their target, this means that although the weapon is
moving quite fast compared to the aircraft a few moments after launch,
atmospheric drag and maneuvering can significantly slow the missile down
before it covers the distance to its target. This means that if the
aircraft can build up enough speed, it can literally outrun the missile.
Since missiles can only travel so slow due before stalling or their
guidance systems can only run so long before their batteries die, the
weapon can be rendered ineffective.

If a SAM is fired at a close enough range where it has enough energy to
still catch up, the other option a pilot has would be to try to defeat
the weapon by putting something between itself and guiding radar. This
strategy works if the terrain allows it, the aircraft has enough to get
to the proper altitude and if the missile launched from SAM battery does
not have on-board guidance that can hold onto the target.

The final option, also simulated in COMMAND is attempting to
kinematically defeat the missile through aggressive maneuvering close to
the time of impact. It can be possible through beaming or a high-g
maneuvers to create a condition where the missile does not have enough
energy or guidance to match the sudden maneuver. This is often a
last-ditch maneuver when other means of defeating the incoming missile
is not possible. COMMAND simulates these techniques based on the range
of the missile to the target aircraft and the available energy.

When aircraft are used in formations, many different options control the
behavior of the wingmen when responding to contacts. AI wingmen can be
told to engage and investigate unknown targets and in order to keep them
'in line', COMMAND calculates all distances based on the formation LEAD
as opposed to the entire group.

### 9.3.2 Naval Combat

With naval guns, accuracy is highly dependent on the type of fire
control setting, the range to the target, and the stability of the gun
platform. A combination of calm seas and a heavy ship does wonders for
accuracy, while a light ship bouncing in rough waters is the opposite.
They may both be firing naval guns that are very similar or even exactly
the same, but a small patrol vessel with manual control alone in very
wavy seas will not hit as well as a large cruiser or battleship in a
calm ocean with intact, advanced fire control systems.

With missiles, the target has more of a chance to defend itself. The
first line of defence is to try and shoot the missile down. This is a
task dependent on the quality of both the launcher and target. Some
weapons systems may be unable to engage low-flying or fast enough
missiles at all, while others will struggle and have a low probability
of success. The second is to deploy countermeasures (chaff/flares and
DECM), which work similarly to those on aircraft.

The OODA clock of the target, affected by its technological
sophistication and proficiency, also plays a gigantic role. The OODA
clock and speed of the attacking missile determine how many shots the
defender can fire before the missile hits-or if they even can fight back
at all. An old and/or slow system may be completely helpless against an
oncoming threat. No one said naval combat was fair.

(*In real life, since anti-ship missiles were invented, there has been a
debate about 'sneakers' vs 'streakers', whether it's more effective to
have a missile rely on stealth or speed to overwhelm the opponent's OODA
cycle. Command gives you the opportunity to test it out in all sorts of
conditions.)*

### 9.3.3 Submarine Combat

Submarines are similar to surface ships in many ways, and outright
identical if they're old-style "undersea boats" engaging on the surface
with deck guns. But they're also very different in two important areas.

The first is that submarines are both stealthier than nearly all surface
ships and have worse "vision". This largely applies even in extreme
cases. Noisy first-generation nuclear submarines still have
characteristics no surface ship can match, and modern ones with
ultra-advanced sonar still can't see nearly as far as a networked
surface combatant. The second is that, surrounded by crushing water,
submarines are incredibly fragile. There's a reason why submarine crews
ranked at the top of the proportionate casualty lists in the World Wars.

Thus, it's important not to get detected if possible. Use of the thermal
layer (see below) is important. So is the realization that a submarine
can be inferred and moved against even if it cannot be detected. Both
inbound torpedoes ("torpedo datum") and ships suddenly suffering an
undetected torpedo hit ("flaming datum") will cause a submarine contact
to be generated for the "victim" side. Likewise, a submarine-launched
missile observed leaving the water will create a contact next to the
spot where the launch was detected.

Submarines come in diesel and nuclear varieties. Although most of the
gap has been closed in present times, earlier nuclear submarines are
incredibly noisy compared to their diesel counterparts. Furthermore,
their reactors and pumps mean that they remain loud even when stationary
or moving very slowly.

However, what the nuclear submarines lack in stealth, they more than
make up for in terms of speed. Not only can most of them move faster
than comparable diesel submarines, but all of them can move
*consistently* faster. Whereas as a submerged diesel running at full
blast will burn through its batteries extremely quickly, a nuclear
submarine can keep going and going like a certain battery mascot.

Moving quickly is an effective strategy against submarines, especially
diesels. However, not all HVUs in an area may be able to move fast
enough to follow that strategy.

Submarine sonars get a clear picture only with a "direct-path" contact,
a fairly close area to the sound, roughly analogous to the visual
horizon. In deep water, a submarine with a powerful sonar may have a
series of green rings around it. These represent the convergence zones.
Units entering the convergence zones can be detected by the sonar,
although their uncertainty zone is far wider than it would be under a
direct-path contact.

In shallow water, convergence zone contacts are not possible. This is a
known limitation of submarines in the littorals, and the other side of
the effects that also make them deadly.

**Understanding Depth Bands and the Thermal Layer**

What follows is a brief summary of how the different depth ranges
(reflected on the depth-presets on the unit throttle/altitude window)
are modeled in COMMAND, and the tactical implications of each.

Towed arrays and/or VDS systems are represented by the red tails on each
platform.

**Periscope depth**: This is the only depth at which subs can use their
above-water sensors (periscope, ESM, radar etc.). A strong surface duct
is usually present, which magnifies the transmission range of noise well
beyond nominal (in fact, in calm seas a surface ship can use this duct
to get early warning of threats that are visually/electronically
stealthy but acoustically very noisy, such as small high-speed boats).
Bad weather significantly degrades this duct's effect. All sub-launched
missiles can be launched at this depth. Because of the small water
pressure cavitation sets in even at relatively low throttle settings.
This is the optimum depth for detection against surface ships (and
counter-detection by hull sonars on surface ships, as well as
"shallow"-set sonobuoys and dipping sonars).

**Shallow**: Some (but not all) sub-launched missiles can be launched at
this depth. The surface duct is still present but significantly weaker.
This depth is suitable for keeping an eye (or ear, as it goes) on
surface traffic and staying near (or at) missile-launch conditions while
keeping out of the strong surface duct (reduce counter-detection by
air/surface) and keeping close to the layer below for a quick dive if
necessary (ditto).

**Just above layer**: Completely out of the surface duct, this depth
reduces interaction with air/surface matters even more, at the benefit
of ASW. Indeed, this is the ideal hunting ground for ASW-oriented subs
with towed arrays. This is because subs at this depth automatically
trail their arrays *below* the layer; thus, they maximize their
detection range against anything below while masking themselves with the
layer (and retaining their above-layer search ability with their hull
sonars). Cavitation speed is significantly higher here. No missiles can
be used at this depth or below.

**In-layer**: Like above, the towed array hangs below the layer, but the
counter-detection reduction is not as great (sound has to go through a
lot less to reach an enemy sensor). Also, the unpredictable mix-up of
warm and cold water at this depth range significantly reduces detection
ranges against other subs also in the layer (think Mutara Nebula from
Star Trek II).

**Just under layer - the Deep Sound Channel**: This is by far the most
transmission-friendly depth band, greatly magnifying detection ranges.
Surface ships and subs just above the layer both trail their VDS or
towed arrays in this band. Sonobuoys and dipping sonars in "deep"
setting also operate here. As a result, this is the worst place to be if
you are hunted by modern ASW forces (or conversely, the best place to be
if you want to attract attention). As a consolation, cavitation speed
rises even higher. ASW-tasked subs without towed arrays often loiter in
this band to maximize the range of their hull sonars. Surface and
shallow sonars as well as "shallow"-set sonobuoys and dipping sonars
have their ranges drastically cut against under-layer targets, and in
some cases may not be able to get through at all.

**The Great Deep**: The DSC still has some influence here but not as
great. Cavitation sets in only if you go flat-out (modern subs do not
cavitate at all here, even at flank). If the sea bottom is shallower
than the sub's rated depth, the sub can "fly nap of the earth" or
even go belly-up (sit on the bottom) and get the benefit of greatly
reduced active sonar echo. This is generally the ideal depth for
"transit" mode, when the emphasis is on moving from A to B rather than
hunting, or for stationary ambush.

Please note that the layer ceiling and bottom, as well as its
"thickness" (and hence absorption rate) are not fixed, but vary
according to latitude, local depth and local temperature (the estimated
actual values are shown on the map cursor). Trying to manually keep a
submarine at the edges of the layer as these values shift can be a very
tedious job, hence the depth presets which automate this.

**Convergence Zones in Command**:

- CZ detections are possible only if the local depth provides at least
  600ft/200m clearance under the target.

- CZ information (range estimates) is displayed on the map mouse cursor
  right alongside the thermal layer info.

- CZ intervals range from 40nm in the poles to 20nm in the equator,
  depending also on local temperature.

- An arbitrary number of CZs are supported, if the sound is powerful
  enough and the receiver sensitive enough. Maximum direct-path range is
  20k yards (\~9.5nm).

- CZ area depth (i.e. ring thickness) is assumed to be 5nm, so the
  actual detection range at each CZ interval may be plus/minus 2.5nm.

To verify if CZs can indeed form between the sensor and target, we check
not only their respective local depths but also the depths at the nadirs
of each CZ curve; so for example the sensor and the target may both have
an abyss below them but if an underwater ridge high enough is between
them it may well block the CZ path.

Sonar operators are assumed to be proficient enough to discriminate
between a direct-path contact and a CZ one (by examining both aural
tones and the bearing rate); as a result, the generated AOU will either
start from the sensor platform and extend to max direct-path range, or
(in the case of a CZ detection) start from the innermost CZ interval and
extend to max sensor range.

### 9.3.4 Mine Warfare

Since World War II, naval mines have sunk or damaged more ships than any
other weapon. Immense resources have been directed into both creating
and neutralizing minefields. COMMAND thus includes an exhaustively
modeled mine warfare system.

There are two ways of laying mines in COMMAND. The first is the "prefab"
way in the scenario editor. Create a box of reference points, make sure
that they're selected, take note of the water's depth in the highlighted
area, and then go to "Minefields" in the editor drop down menu. Select
"create minefield in designated area" and a menu will appear containing
a long list of naval mines in the current database. These range from
named specific mines to a list of "generic mines" of various types. The
important kinds are:

- Moored mines. The most stereotypical naval mines, these can be laid at
  a fairly great depth thanks to their moorings keeping the warhead at a
  dangerous level. However, the moorings also make them easier to spot
  (and therefore neutralize).

- Bottom mines. These, true to their name, sit at the bottom of the sea.
  They are lower profile than moored mines and thus hard to detect, but
  because they depend on their blast wave reaching the surface, they
  have to be laid in shallow waters only. Some bottom mines are
  "mobile", deployed by "swimming" out of torpedo tubes at a standoff
  distance before stopping.

- Floating/drifting mines. These stay on the surface and are thus the
  most visible. Floaters are very difficult for aircraft to take down.

- Rising mines. Arguably the most dangerous type of mine, rising mines
  sit on the bottom and then release a payload when they detect their
  target, which can be an unguided rocket or a homing torpedo like the
  CAPTOR. Rising mines combine the stealth of bottom mines with the
  deployment depth of moored mines, making them highly dangerous.

Once the type of mine is selected, choose the number to be deployed (if
in doubt, add more), and press "ADD". The editor will deploy as many
mines as it can in an irregular pattern. Frequently there will be less
than the stated number deployed even if the water is shallow enough.

The second way is via a minelaying mission. See **7.2.5 Mining Mission**
on page [156](#mining-mission). Use air or sea units with a mine loadout
(for the latter, mine weapons records can be added to existing units if
need be) and execute the mission.

In both types of minelaying, the deployment will be uneven and seemingly
erratic. This is deliberate to ensure that opponents can't accurately
guess the minefield's location after detecting a few of them. Especially
if it's a prefab layout, make sure the mine placement is satisfactory.
If it isn't, then removing the minefields via the "remove mines from
designated area" function may be necessary.

Once the minefields are placed and units head towards them, calculations
begin when the units get close enough. Its detonation/payload release
distance will depend on the type of unit and sophistication of the mine.
An under-the-keel blast is highly dangerous and will destroy most ships.
A distant blast may not be much on its own, but several can still be
cumulatively damaging.

To counter mines requires ships and aircraft with the appropriate
systems. Countering mines is conducted via mine counter missions (see
**7.2.6 Mine-Clearing Mission** on page [157](#mine-clearing-mission)).

- The two types of mine countermeasures are sweeping and hunting.
  Sweeping involves deliberately activating the mines via sweeping gear
  (visible in the DB viewer and on the map when activated) so that they
  will explode at a less lethal distance. Many types of mines are
  unsweepable and have to be neutralized one at a time via the more
  painstaking mine hunting (having a diver/ROV destroy the mines).

- Mine warfare vessels are expected to get banged up by the blasts as
  part of the job. For sustained scenarios, having a 1 /3 Rule mission
  and a port where minesweepers/hunters can be repaired is strongly
  recommended. A mission *without* the 1/3 rule can be used for an
  emergency surge, if need be, but this is a game of endurance.

- Aircraft tend to be worse at detecting mines but better at destroying
  them, and the reverse is true for ships (thus they complement each
  other). While less vulnerable, low flying aircraft can still be
  damaged/destroyed by detonating mines.

- Unmanned vehicles are ideal for mine hunting due to less crew risk,
  but they have some limitations, such as having no on deck to shoot
  floating mines.

- For mine clearing missions, a narrow safe corridor is better than a
  too-wide area that leaves too much room for mines to slip through.

### 9.3.5 Land Combat

Land combat in Command is currently very basic and works similarly to
naval combat in terms of accuracy with gunfire or missiles. Land units
are intended more as targets for air and sea units than as formations
capable of credibly fighting each other on their own.

This should not discourage scenario writers, for land units can still be
very important. They can still fire and move, and the role of target is
an important one. The offensive capability of land units is not
incompatible with a role as a target-after all, you might be tasked to
destroy a group of "target" AFVs before they destroy your airbase or
other high-value unit. (After all, as the saying goes, "the most
effective air superiority weapon is a tank sitting at the end of the
enemy's runway".)

The terrain a land unit occupies (visible on the databox) has a massive
effect on both its speed and its resistance. Swamps reduce movement
dramatically. Forests slow movement down and provide a level of
shielding from bomb/shell blast effects. Built-up areas add a high level
of shielding but also make land units able to go faster due to their
paved roads.

Land units have the capability of replenishing like UNREP-capable ships.
For example:

A missile battery unit is near an ammo truck unit that has the
appropriate missiles in its magazines. Once the battery has launched and
is out of missiles, the player right-clicks on the battery unit and
selects "replenish (if possible)" from the dialog. Whether the choice is
to automatically or manually select the unit, the process will start.
The missile battery will move alongside the ammo truck, stop, and
restock. One the process is complete; it may fire again.

When aircraft engage a land or naval target with unguided weapons, the
calculation for hitting depends on the target's speed, the properties of
the weapon, the bombsight quality of the aircraft, the altitude of the
aircraft, and the proficiency of the aircraft's crew. A WWII-vintage
fighter crewed by novice's nuisance-bombing at high altitude is going to
be far less accurate than an ace plane with a high-end ballistic
computer flying low.

### 9.3.6 Electronic Warfare

There are two types of electronic countermeasures in COMMAND: Defensive
(DECM) and offensive (OECM).

DECM functions very simply. When a weapon with an appropriate seeker
type closes on a unit with the DECM equipped, it functions as part of
the weapon endgame calc. Whether the DECM can spoof the oncoming weapon
depends on both random chance and the generations of both the DECM
device and the seeker attacking weapon. An old DECM jammer will not have
a good chance of stopping a weapon with a modern seeker and vice versa.

OECM projects out "noise" jamming. This has its strengths compared to
the focused DECM. It can affect multiple units on the map, confusing
search radars. However, it also has its weaknesses. First, ESM can often
detect jamming as an emission unto itself, giving the position of the
jammer. Second, it is very dependent on geometry and positioning, in
addition to the technology level of both the jammer and target(s).

So, if a jamming aircraft is supporting a flight of strikers, it's
highly advisable to position it directly behind them, on a
course/mission that makes it stay as close to that spot as possible. It
should also be as close as possible to the target while still comparably
"safe".

OECM does not currently affect endgame calcs directly the way DECM does,
but (again, depending on the sophistication/strength of the jammer, the
sophistication/strength of the opposing radar system, and the position
of both), it can make SARH missile attacks fail due to disrupting the
radars or make the target location so imprecise that the opponent never
launches to begin with.

### 9.3.7 Damage and Repairs

A unit that is damaged but not immediately destroyed will suffer in
terms of performance and may catch on fire, or (for ships) flood.

While one of them is active, the unit's damage status will continue to
increase, and if either of them reaches the maximum level, the unit will
be automatically destroyed (it either burns out of control or becomes
filled with water and capsizes), regardless of its damage status.

The crew will attempt to control the damage and repair it to the best of
their ability, but their ability to do this in practice depends
massively on circumstances, such as:

-Crew proficiency. As historical evidence shows, this can have a massive
effect on whether or not a ship can survive a hit.

-How fast the unit is moving. Something strained by running at full or
flank throttle will be more vulnerable.

### 9.3.8 My @#%\^@#% weapon won't fire!!!

COMMAND makes few (if any) compromises when it comes to the various
factors affecting weapons and their effect on targets, as well as their
employment. As a result, you may find yourself in a situation where it
is not immediately obvious why the unit you just ordered to engage the
enemy is not firing yet.

A very effective method of getting good feedback on weaponry limitations
is to perform a manual weapon assignment. Your virtual crew runs the
available weapons through an exhaustive checklist of conditions that
(depending on the weapon and target) have to be met before the weapon at
hand can be fired. Some weapons (such as wired guided ones) require that
the launcher itself is not occupied by a new weapon as long as the
current fired weapon is active. This means that reloading (and firing
another one) is not possible until the situation is rectified.

Here is a summary of the no-fire explanations, what they mean and what
you can do as a player to overcome them:

· **Weapon mount is not operational**: The weapon mount (gun, missile
launcher, torpedo tube etc.) holding the weapon in question is out of
action (probably damaged or destroyed) and cannot fire.

- Solution: Be patient until the mount is repaired (if not destroyed
  outright). If possible, have the weapon unloaded from this mount so
  that it can be transferred to another suitable one, if such exists.

· **Unit is not authorized to use nuclear weapons**: The unit as
attempting to fire a nuclear weapon but has no authorization to do so.

- Solution: If you can (you are usually not allowed to), set the unit's
  "Use nukes" doctrine setting to "Yes".

· **Target speed [target speed in knots] is much higher than the
weapon's maximum target speed ([weapon maximum target speed in
knots]):** This applies mostly to SAMs and ABMs. Most such weapons have
a limit to how fast a target they can intercept, either because of
kinematic limitations or because their seekers and guidance systems can
cope with only so much weapon-to-target closing speed. For example, most
versions of the Patriot SAM can intercept tactical ballistic missiles,
and the latest PAC-3 versions can tackle medium-range ballistic
missiles, but ICBMs are a no-no.

- Solution: None really, unless the target somehow reduces speed. Use
  another weapon if available.

· **Target altitude ([target altitude in meters]) is higher than the
weapon's ceiling ([weapon maximum target altitude in meters]):**
Quite simply, the target is flying too fast for the weapon to reach up
and intercept it.

- Solution: None, unless the target later descends. Use another weapon
  if available (there's a reason why, once more advanced low-range air
  defenses proliferated, attack aircraft began flying at high altitude.)

· **Target altitude ([target altitude in meters]) is lower than the
weapon's minimum engagement altitude ([weapon minimum target altitude
in meters])**: Most SAMs have a minimum engagement altitude below which
their guidance systems suffer disproportionally from ground clutter and
other factors. If the target is below that altitude, then the weapon
cannot engage.

- Solution: Wait for the target to rise higher or use another weapon if
  available (there's a reason why flying low during the period of early
  SAMs with low ceilings was considered important).

· **Weapon is not BOL-capable**: The unit is attempting a BOL
(Bearing-only Launch) shot but the weapon does not support this.

- Solution: Execute a direct (non-BOL) shot or use another weapon that
  does have the ability.

· **Weapon needs a precise target location**: Related to BOL ability or
lack thereof, this weapon needs a precise target location instead of an
ambiguous estimate in order to have a reasonable chance of damaging the
target. Guns usually fall into this category, as do other weapons like
ASW rocket launchers.

- Solution: Obtain a precise target location and use the weapon or use
  another weapon that is more tolerant of target ambiguity.

· **Weapon is not loaded on mount**: The weapon is present on the unit
but not loaded on any of its mounts (e.g. stored in one of the
magazines).

- Solution: Wait for weapon to be loaded on mount; if necessary, assign
  reload priority to it.

· **Weapon is not suitable for this target**: The weapon is generally
not suitable for this target type (e.g. torpedo against aircraft)

- Solution: None; use another weapon if available.

· **Altitude too high (Valid: [weapon minimum launch altitude] to
[weapon maximum launch altitude])**: Frequently happening with
aircraft but can also apply to submarines. The unit is high above the
weapon's launch envelope.

- Solution: Dive until you are within launch parameters.

· **Altitude too low (Valid: [weapon minimum launch altitude] to
[weapon maximum launch altitude]):** Flip-side of above; the unit is
too low/deep to use the weapon.

- Solution: Rise up until you are within launch parameters. (Careful!
  You usually go deep/low for a reason - to stay out of enemy
  sensors/weapons. Coming up may mean attracting the wrong kind of
  attention.)

· **Target is outside weapon boresight limits**: This is usually a
problem with forward-firing weapons on aircraft (guns, rockets etc.) but
may also manifest with fixed-azimuth (non-turreted guns).

- Solution: Maneuver the unit so that the target is within boresight
  limits (typically dead ahead of the unit's front).

· **Target aspect ([target aspect in degrees]) is out of envelope for
a stern-chase weapon**: Most often a problem with early AAMs but also
certain old torpedoes: The weapon is not very maneuver-friendly and
needs to be fired almost directly behind the target.

- Solution: Instead of the weapon, the unit will have to do the
  maneuvering; position it as much directly behind the target as
  possible.

· **Target aspect ([target aspect in degrees]) is out of envelope for
a rear-aspect weapon**: Similar to the above, but with less tight
constraints.

- Solution: As above; get behind the target (or off to the side) and
  launch the weapon if possible.

· **Weapon cannot engage this target for another [time value in sec]
(OODA loop limitation)**: Each unit has a certain delay between first
detection of a contact (or being given its data from elsewhere) and
being able to target and engage it (the so called "OODA loop" -- yes,
the one from John "40-second" Boyd). With surprise threats this delay
can often be fatal.

- Solution: None really, just hope that the countdown runs out before
  the target becomes an imminent threat. If it is already an imminent
  threat (e.g. incoming anti-ship missile) and it looks like it's
  beating the clock, hope that the unit has automated point-defense
  systems that can ignore the OODA countdown and engage it. If not...
  brace for impact.

- (NOTE: As a *scenario designer,* this problem can be mitigated by
  increasing the proficiency of the unit/side. Higher proficiency units
  have a shorter OODA clock)

· **ASW torpedo must be dropped within 0.5nm of contact/aimpoint**: ASW
torpedoes must be dropped close to the estimated target submarine
position in order to have a fair chance of catching up to it before
running out of fuel.

- Solution: Get closer to the sub's estimated position and drop.

· **Target is out of weapon's range**: Quite simply, the target is out
of this weapon's maximum range.

- Solution: Get closer (which may be easier said than done) or use a
  longer-ranged weapon.

· **Target is within weapon's minimum range**: Flip-side of the above;
the weapon has a non-trivial minimum firing range, and the target is
within it.

- Solution: Open the distance or use another weapon without the minimum
  range limitation.

· **Horizontal range to target ([range to target in nm]) is greater
than the weapon's downrange at this altitude ([weapon downrange in
nm]):** This most often happens with aircraft-launched ballistic
weapons (guns, rockets, unguided bombs etc.). The higher the altitude of
the carrier aircraft, the greater the distance at which it can literally
toss the weapon towards the target. At higher altitude this distance
shrinks dramatically.

- Solution: Get closer or rise to higher altitude to increase toss
  range. Both these options carry counter-detection/engagement risk so
  choose carefully (or use another weapon with better standoff).

· **Target is within 5 nm and outside the weapon mount's engagement
arc**: This typically applies to ship turrets/launchers. Command
currently ignores mount arc limits for engagements at distances over
5nm; the implicit assumption is that at such distance's captains
micro-maneuver their ships to unmask their weapons as necessary, and
often even perform "over the shoulder" shots with guided weapons.

At distances below 5 nautical miles however, there is no time or space
for maneuvers and shot-tricks; a ship engages a threat only with the
weapons it can bring to bear down the threat's azimuth. This can make
life difficult for large ships trying to engage smaller, more agile
opponents or pop-up threats like sea-skimming anti-ship missiles.

- Solution: Try to turn around so the weapon you want to use is
  unmasked. If the target is a high-speed incoming threat (torpedo,
  missile e.g.) you have very little available time so this may possibly
  not work.

· **Cannot fire weapon through ice**: You are attempting to engage a
target through the ice pack (e.g. shoot at a submarine with an
air-dropped weapon).

- Solution: None. If possible, wait until the target moves from under
  the ice before trying to engage again.

· **Cannot fire missile while under ice**: You are attempting to fire a
missile from a submerged submarine under the ice.

- Solution: None. Move the submarine out of the ice if possible.

· **Cannot use torpedo on ice**: You are attempting to drop a torpedo
from an aircraft/helicopter to an under-ice submarine.

- Solution: None.

· **Gun has no local control and no available directors**: The gun is
designed to work with a fire-control sensor on the same unit which is
currently out of action (for any number of reasons: Damaged/destroyed,
jammed, cannot detect target etc.), and it (the gun) has no local/manual
control as backup. It is essentially "blind". NOTE: This limitation
appears only if you have enabled the "Detailed gun fire control" realism
setting.

- Solution: If the FC director suitable for the gun is functioning but
  unable to detect the target, do anything necessary to allow it to do
  so (counter jamming, change heading to unmask director etc.).
  Otherwise use another weapon if possible.

· **Weapon must detect target prior to firing**: The weapon must "lock
on" to the target on its own prior to launch and cannot be fired
"blindly" with the expectation of post-launch lock. Most IR-guided AAMs
fall in this category.

- Solution: Position the firing unit in optimum position for the weapon
  to detect the target (e.g. in a dogfight, try to get on the target's
  tail as much as possible). The weapon will do the rest.

· **No weapons director available to illuminate the target**: The guided
weapon (usually missile) needs a compatible FC director to provide
illumination to the target in order to guide the weapon, and no such
sensor can be found (in an operative state). Similar to gun-fire control
limitations.

- Solution: If the FC director suitable for the gun is functioning but
  unable to detect the target, do anything necessary to allow it to do
  so (counter jamming, change position to obtain line-of-sight etc.).
  Otherwise use another weapon.

· **All illumination channels suitable for this weapon are in use**:
Related to the above; we found a suitable FC illuminator for the weapon,
but all available illumination/guidance channels are in use (i.e. the
system is already locked on to its maximum number of targets and can't
engage any more).

- Solution: This indicates that one or more engagements are currently in
  progress. Wait for the engagement(s) to conclude so that the
  illumination/guidance channels can be freed up.

· **All directors are unable to illuminate this target (insufficient
reflection, no LOS etc.)**: The guided weapon (usually missile) needs a
compatible FC director to provide illumination to the target in order to
guide the weapon, and no such sensor can be found (in an operative
state). Similar to gun-fire control limitations. This is frequently
observed with guidance radars against low-observability targets (in
fact, the F-117 was created to be resistant to guidance radars first and
search radars second).

- Solution: If the FC director suitable for the gun is functioning but
  unable to detect the target, do anything necessary to allow it to do
  so (counter jamming, change position to obtain line-of-sight etc.).
  Otherwise use another weapon or see if the target moves closer.

· **No datalink channel available to guide this weapon**: The weapon has
a mandatory datalink (such as the guidance wire on a TOW anti-tank
missile) and no channel is currently available.

- Solution: This indicates that one or more engagements are currently in
  progress. Wait for the engagement(s) to conclude so that the datalink
  channels can be freed up.

· **Target is out of weapon's DLZ**: The target is out of the weapon's
dynamic launch zone (DLZ; see **9.3.9 DLZ and Why It Matters** on page
[214](#dlz-and-why-it-matters)).

- Solution: Get closer to the target or wait for it to change its
  heading/speed/alt so that it falls within the weapon's DLZ.

· **The target's downrange ambiguity ([weapon downrange ambiguity in
nm]) is larger than [some percentage] the weapon's acceptable limit
([weapon acceptable downrange ambiguity in nm]):** This is directly
related to the "Shooting ambiguous targets" doctrine setting. If the
target's uncertainty area is such that its range ambiguity towards the
firing unit is too large, the weapon will not fire. For example, if the
target's distance has a +/- 10nm margin of error, and the weapon has an
acceptable limit of 2nm (seeker limit, warhead damage area etc.) then
the unit will refuse to fire.

- Solution: If you can (you may not be allowed to), set the firing
  unit's "Shooting ambiguous targets" doctrine setting to "Optimistic"
  or even "Ignore". This will make the unit all too happy to use the
  weapon against the target even with a large margin of error. Beware
  that this means a large probability that the weapon will miss
  altogether. Ignore is not recommended against targets that have
  visibly moved at all.

· **The target's downrange ambiguity ([weapon downrange ambiguity in
nm]) is larger than [some percentage] the weapon's acceptable limit
([weapon acceptable downrange ambiguity in nm]):** As above, this time
with regards to target cross-range instead of distance ambiguity.

o Solution: If you can (you may not be allowed to), set the firing
unit's "Shooting ambiguous targets" doctrine setting to "Optimistic" or
even "Ignore". This will make the unit all too happy to use the weapon
against the target even with a large margin of error. WARNING: Large
angular margins of error mean that you have to be really lucky to get a
successful hit.

### 9.3.9 DLZ and Why It Matters

When firing a guided weapon against a target, we want to have a
reasonable probability (if not certainty) that the weapon will reach the
target. Against static or slow-moving targets this is a straightforward
affair; against high speed and/or agile targets, however, things can get
more complicated.

One of the simplest concepts of estimating a weapon's reach against a
moving target is the so-called "No-Escape Zone" or NEZ. This assumes
that at the moment of weapon fire, the target turns tail and runs at its
current known speed directly away from the launch point. The weapon then
has to run the target down in a straight line.

The simplicity of NEZ made it attractive for early missile fire-control
computers and indeed it remains a widely-used yardstick when comparing
the kinematic performance of weapons such as AAMs/SAMs, torpedoes etc.
However, in real combat units rarely detect incoming weapons immediately
at launch and not often turn tail and run away -- at least not if they
have a job to do. The NEZ is also meaningless against targets that
naturally don't run away, such as cruise missiles and UAVs (and
non-alerted targets of any kind, e.g. very frequently ships under
torpedo attack).

Relying exclusively on NEZ is can also represent a "hidden" tactical
liability. Consider an F-15 fighter preparing for a Sparrow AAM shot
against a high-speed incoming MiG-25. Following NEZ's logic, the MiG's
high speed means that the missile must be launched at very close range
in order to successfully perform the hypothetical run-down that the NEZ
is built upon. However, we instinctively understand that this logic is
flawed: The F-15 pilot should instead launch the Sparrow at an even
longer-than-nominal range, taking advantage of the MiG's high incoming
speed and using it against it.

So what we need is an engagement zone concept that takes into account
additional parameters known about the target such as its current heading
and altitude. This concept is the Dynamic Launch Zone or DLZ.

Fundamentally, the conceptual difference between NEZ and DLZ is clear.
NEZ answers the question: What will happen if I launch right now, and
the target turns right away and runs? DLZ answers the question: What
will happen if I launch right now, and the target keeps moving as-is?

The DLZ is harder to calculate for two reasons.

The first one is fairly obvious: Unless the target is coming head-on or
running straight away, the engagement geometry is significantly more
complex. The second reason is that in order to answer the question
faithfully, the algorithm must consider the kinematic & guidance
idiosyncrasies of the weapon in question. Some weapons head straight for
their target at a near-constant speed; others deliberately opt for a
parabolic loft; yet others employ subtle guidance tricks tailored to the
nature of both the weapon's role and the characteristics of the nominal
target the weapon was designed for. All these nooks and crannies must be
taken into account or else the DLZ calculation may well be off.

Command employs several algorithms for faithful DLZ calculations, some
tailored for aerodynamic targets (with special options for
non-maneuvering targets such as cruise missiles) and others optimized
for orbital & ballistic targets such as ballistic missiles, re-entry
vehicles and satellites. You will notice that AI crews are usually quite
careful not to fire weapons at the extreme edge of their range envelope,
preferring to sacrifice a slice of standoff for the sake of ensuring a
kill. There still will be outliers though, taking their chances will
long-range "sniper" shots that can still do damage.

It should be emphasized that in the case of maneuverable targets, being
inside the DLZ does not guarantee that the weapon will reach out to the
target -- after all, an alerted enemy may (probably will) not cooperate.
But even if a shot is dodged, it still puts the target on the defensive.
The top Serbian MiG-29 pilot in the Kosovo conflict was finally shot
down after successively avoiding 3 AMRAAM shots in a single engagement
-- each time surrendering more of the initiative to his attackers, never
having a chance to shoot back.

### 9.3.10 A Note on Losses

No unit is indestructible, and operational planning frequently matters
far more than the exact quality of the unit. It is entirely possible for
a MiG-21 to destroy an F-15 if it gets a clear shot.

Much of the "turning/burning" parts of air combat are abstracted by hit
rates and crew proficiency. The part of the human element the player can
control is getting the assets to the right place at the right time. An
example of the dichotomy between tactical weakness and operational
strength is in the 1972 air campaign that beat back the Easter Offensive
in the Vietnam War.

In that, the kill/loss ratio of USAF aircraft reached new lows, with
them having a negative rating even by their own admission during various
points (meaning the true total was almost certainly even worse). Yet
this mostly consisted of North Vietnamese MiGs nibbling away at the
outer escorts-despite their weaknesses, they did their job of keeping
the strikers safe. In Command, you can do the same.

Even in scenarios intended to re-enact historical battles or wars, the
results are frequently much different from the actual outcome. This is
to be expected. While a bug report (see **1.2 Support** on page
[4](#support)) may be in order if the historical result is *never*
obtained even once, variation is normal and good.

Command's engine is intended to be able to simulate everything from
1940s broadside duels to futuristic satellite-cued ballistic missile
strikes with a reasonable degree of success, not be incredibly accurate
for any one conflict. To return to the Vietnam analogy, the performance
of similar, and frequently the exact same aircraft and weapons varied
widely by conflict. There was Vietnam, the Indo-Pakistan, and
Arab-Israeli Wars in the same time period.

Attempting to model any one of these conflicts with one hundred percent
razor-sharp accuracy would make any of the others less effective. One
would be faced with either an a historically strong Egyptian/Syrian Air
Force or an a historically weak North Vietnamese one if a strict model
intended for one was used for the other.

In addition, real events can only happen once, while the simulator can
be run many times. The real result may have been a one-in-a-hundred
"outlier", while the most common one may have been quite different.

## 9.4 Construction and Destruction

### 9.4.1 Building and Destroying Air Bases

Air Bases are important units in COMMAND. They can be added to scenarios
either as a single unit or air base group. At the basic level they host
aircraft, but they also support the simulations advanced aircraft
logistics and sortie models and act as advanced targets. This section
explains how to build these units and how to destroy them.

Air bases are currently implemented in the game as either one very
generic single-serving unit (Single-Unit Airfield) or as an airbase
group that could include hundreds of individual facilities. As a
designer you can choose the type you would like to use but unit-count
does impact performance so it's best to use a single-unit airfield
unless the air base has the potential to be a target. There is no
difference in function between the two. COMMAND'S databases provide a
ready selection of such bases in various sizes (going all the way up to
multiple 4000-m runways) so you can select what most closely fits your
needs.

COMMAND'S air bases do model aircraft traffic, which helps support the
simulation accurately model aircraft-sortie rates. When given a launch
order, aircraft will start in their holding facilities such as tarmacs,
hangars or revetments, move to a connecting/transit facility such as a
Runway Access Point or Taxiway (or elevator in a ship) and then move to
a Runway where they are launched. When they land, they step back through
the flow to their holding facility, receive replacement fuel and
ammunition and then start the process again. This helps generate
realistic sortie rates which we feel are critical in modelling modern
air warfare. It also makes airbases critically dependent on a few key
nodes being operational -- or, put from another perspective, if an enemy
damages or destroys certain facilities he can shut down an airbase with
much less effort, just like in real life.

Air bases currently support the aircraft logistics model in the game.
All air bases include ammunition magazines which players can populate
with the weapons, pods, tanks and equipment that aircraft need to
successfully host their various loads. Fuel is not currently tracked but
is provided automatically when an aircraft lands. As such, scenarios
that exceed the flight time or an aircraft must include an air base or a
ship capable of hosting aircraft or the aircraft will ditch (and be
destroyed) when its fuel has been expended.

For more information on how to populate ammo magazines please review
section 5.3.1 of the manual. It is highly suggested that you use the
"Show only weapons compatible with aircraft hosted by parent" filter in
the Add Weapons dialog to assist with finding the correct weapon-records
to add.

**Constructing an Air Base**

Constructing an air base group is accomplished in a similar manner to
building other groups in the game. You should add the individual
facilities and then group them by selecting them all and pressing **the
g key**.

It is highly suggested that you use our "Custom Overlay" feature to get
a properly sized and sited image of the facility you are adding on your
game map. This allows you to simply add the needed units where you see
them in the image -- easily and with extreme accuracy.

Once you have constructed the base, you can then use the import/export
unit feature to save it for future use. We have already constructed
thousands of airfields, airbases and airports which you can import into
the game, so it is best to check first before spending too much time
building your own.

The databases have tons of air base facilities but the minimum units
necessary for a functional air base group are as follows:

- 1x Runway long enough to support the aircraft you will base there. You
  can get this by comparing the runway length in the name and database
  viewer entry with the aircraft Take-off/Landing distance field in the
  database viewer.

- 1x Access Point or Taxiway large enough to support the aircraft that
  will be using them.

- 1x Unit Capable of holding the aircraft (Tarmacs, Open Parking Spaces,
  Hangars, Shelters, etc.) you'd like to host there. Units have the
  aircraft size and capacity in their names which you can compare with
  what is listed in the aircraft size field in the database viewer.

- 1x Unit with an ammunition magazine (Ammo Shelters, Ammo Pads, Ammo
  Bunker, etc.)

- 1x Fuel holding facility. We aren't requiring this as we are not
  tracking fuel logistics but may do so in the future.

Adding Single-Unit Airfield airfields is straight forward in that you
just add them as you would any other unit in the game. They include all
the necessary pieces required to function and just require you to rename
the unit to whatever you would like unit to be. These can be saved to
import file and exported back in as well.

Be aware that single-unit airfields are not intended to be targets and
should only be included in a scenario where they will not be attacked.
Thus, a forward airstrip in the heat of the battle should be modelled as
a multi-unit airbase, while a base hosting long-range bombers far away
from any of the opponent's weapons should be modelled as a single-unit
one.

**Destroying or Inhibiting Air Base Operations**

Tying everything, we have learned about the functions of Command air
bases and how to build them, we can now see ways to destroy or
mission-kill them.

Keep in mind that unless the air base is small enough and/or the
attacker strong to simply smother it, determining where the individual
aircraft are is essential. For aircraft parked in the open, this is as
simple as moving a unit with optical sensors close enough to detect
and/or identify them. Under the "contact reports" window, the detected
aircraft will appear under the "Spotted Hosted Units" tab, they will
appear on the message log when detected/identified, and on the map, a
black triangle in a yellow box will mark any facility with hosted units
inside.

For enclosed shelters, things get trickier. The aircraft have to be
spotted entering or leaving them over the course of air operations to
get an identification. This necessitates either persistent surveillance
(like a ground recon team) or good timing.

Methods to Mission-kill or otherwise incapacitate a modern air base:

- **Destroy aircraft holding facilities**: Probably the least efficient
  but you can eliminate all aircraft at the facility by destroying the
  buildings/sites that contain them. Most nations harden these
  facilities or disperse aircraft to make this task difficult. To
  evaluate a weapon's effectiveness against a target please review the
  weapon's legal target values and damage point value (DPs) in the
  aircraft stores section of the database viewer and compare it to the
  target's armor and damage point values.

<!-- -->

- **Destroy Magazines**: Destroying ammo storage facilities prevents
  aircraft from receiving necessary ammunition. A combat aircraft
  without its weapons is only marginally more useful than if it has been
  destroyed. Similar to aircraft holding facilities, most nations harden
  the facilities or disperse ammunition to minimize losses. Note that
  this will not work if unlimited ammunition is enabled in scenario
  settings, so if destroying airbase magazines is important, the
  scenario designer should turn that option off.

- **Disable Access Points, Taxiways and Elevators**: Disabling (these
  facilities cannot be permanently destroyed and will eventually be
  repaired given enough time) these "transit" points prevent aircraft
  from reaching runways or other aircraft launch facilities. Usually
  there are only a few of those in a base or ship so taking them out is
  a great way to jam the base shut.

- **Disable runways**: Disabling these eliminates the ability of an
  aircraft to launch. This is often the most efficient method. Nations
  tend to add secondary runways or use auxiliary runways to make this
  task slightly more difficult. COMMAND supports numerous dedicated
  anti-runway weapons. It should be noted that historically, runway
  attacks have only been useful as "temporary" knockouts to airbases.
  The runway can be repaired quickly just by repaving it, especially if
  it's been hit by non-specialized munitions. As such, many planners
  have aimed for targets other than runways to cause more lasting
  damage.

**Note on airfield damage**: Runways (and other air facilities) have
what is called an "effective runway/AC size", which takes into
consideration both the runway's nominal aircraft size capacity and its
current integrity status, to determine the true AC size class that it
can handle.

Using an airfield with a 350 runway:

\* At between 75% and 100% integrity level (i.e. 0-25% damage), the
runway can handle very large aircraft.
\* Between 50% and 75% integrity it can handle up to large aircraft.
\* Between 25% and 50% integrity it can handle up to medium aircraft.
\* Between 10% and 25% integrity it can handle up to small aircraft.
\* Between 1% and 10% integrity only STOVL aircraft or helicopters can
operate. *(\<--- At this point you're literally looking at craters
and broken chunks of concrete everywhere. Perhaps even the STOVL ability
is optimistic, given that in such a condition the engine-FOD would be
quite likely...)*

A sortie rate slowdown can be observed due to many reasons, e.g. some of
the taxiways being knocked out (if the damage inflicted on the runway is
part of a wider attack on the base). The taxiways and runway access
points are a critical chokepoint and messing with them is a pretty
cost-effective way of throwing the OPFOR's ATO/mission timetables
completely out of the window. (Or simply delaying the GAI launch long
enough that the strike does its job).

### 9.4.2 Building and Destroying Naval Bases

Naval bases are like air bases but require only two facilities for a
minimum functional group: at least one pier and a munitions storage
facility. Expansive facilities are encouraged for the sake of realism
and targeting-big ships require big ports.

Docked naval units at ports can be detected and identified like aircraft
at air bases. The same criterion for observation is there, as is the
same black and yellow symbol indicating a present unit.

### 9.4.3 Building (And Destroying) Air Defenses

Air defense facilities in COMMAND are some of the most important land
units. Anti-aircraft artillery, and, since the Powers U-2 shootdown,
surface-to-air missiles have shaped the landscape of air operations.

- SENSORS: The air defense network needs to be able to see its incoming
  targets before it can hit them. This includes search radars as the
  most obvious component, but a truly effective IADS will also have ESM
  sensors and even visual observers. The search radars are frequently
  kept a considerable distance apart from the launch sites.

- WEAPONS: Anti-aircraft weapons come in three major categories: Low
  altitude, medium altitude, and high altitude. They combine to become
  more than the sum of their parts when properly cited, with the most
  famous example being the North Vietnamese SAMs that did not score too
  many kills on their own-because they made the Americans fly lower,
  right into the teeth of the AAA that claimed the most victories.

  - Low Altitude/Short Range: This includes almost all anti-aircraft
    guns and MANPADS like the Stinger and SA-7.

  - Medium Altitude/Range: This includes medium-sized missiles like the
    SA-6 and Aspide.

  - High Altitude/Range: This includes heavy missiles, whether they be
    early (SA-2 and Nike) or modern (Patriot and S-300 family)

Air defense facilities should cover as many altitudes and angles as
possible. They should be mutually supporting, covering both the defended
area and each other. Placing short range point defense systems around
both longer-range launchers and search radars is recommended,
particularly if the opponent has standoff weapons like Tomahawks. Radars
should not emit unless absolutely necessary.

For the destruction of air defenses, there are two options. The first is
to simply treat them like any other target, engaging them with
conventional strikes and patrols. The second is dedicated SEAD patrols,
which focus on radar emissions. There is no one-size fits all solution
to dealing with air defenses.

## 9.5 Unmanned Aerial Vehicles

UAVs have become a dominant and omnipresent force on the battlefield.
COMMAND models some of the special functionality of the UAVs, especially
how they can operate themselves when they lose contact with their signal
provider. Some UAVs, nothing more than remotely controlled aircraft,
will on loss of signal become "ghost planes," flying off on their last
heading until eventually crashing. Some can self-recover, i.e. search
for a new signal and return to base if reconnection proves impossible.
Newer UAVs are proving increasingly more autonomous, able to complete
their last orders, self-analyze their ability to continue, work
together, or even "think" for themselves. Once this is implemented,
jamming drones will have platform-specific consequences beyond simply
losing communications: some drones will crash immediately, while others
may go off and hunt down John Connor.


