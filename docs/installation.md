# 1.0 Installation

??? info "FAQ: Where can I obtain a copy?"
    Command and its various DLC packs are available on [Steam](https://store.steampowered.com/app/1076160/Command_Modern_Operations/). It can also be purchased as a standalone product (offline installer with serial key) at [Matrix Games](https://www.matrixgames.com/). Buying at Matrix Games also provides you with a free Steam key.

??? info "FAQ: Do I need an internet connection?"
    Command does not require an internet connection to activate or play. However, if you want to upgrade the game to the latest version (which is highly recommended), you will need an internet connection.

??? info "FAQ: What are the recommended system requirements?"
    - **OS:** Windows 10/11
    - **Processor:** Quad-core, 4th-generation Intel or equivalent
    - **Memory:** 8 GB RAM
    - **Graphics:** DX11 compatible GeForce GT 1030+ or equivalent (some iGPUs work well, e.g. AMD Ryzen)
    - **DirectX:** Version 11
    - **Storage:** 40-50GB available space

    Command is first and foremost a CPU-hungry beast. The simulation engine is multithreaded and scales well up to 8 cores. Processors with few-but-powerful cores have an advantage over many-but-less-powerful cores.

??? info "FAQ: Does Command run on Mac or Linux?"
    **Mac:** Command does not run natively on any Mac operating system, but you can use virtualization software like Parallels or VMWare Fusion to run it inside a VM on top of the host operating system.

    **Linux:** Officially, there is no support for running on Linux. However, numerous users have succeeded in running Command on Linux. A pinned thread on Steam discusses how to accomplish this.

??? info "FAQ: Are there any known incompatibilities?"
    Some motherboard utilities and screencasting programs (particularly those working with DirectX overlays) can interfere with Command's execution and distort some of its data windows. Frequent culprits include:

    - RivaTuner
    - Nahimic
    - Nvidia Share
    - MSI Afterburner
    - Discord's "Game Overlays" mode

    If the Unit Status panel gets corrupted when you mouse over it, check if any of these overlays are enabled and disable them.

??? info "FAQ: How can I upgrade to the latest version?"
    There are two ways to upgrade:

    1. **Steam version:** Updates are handled automatically through Steam.

    2. **Standalone version:** Use the "Update" button from the game launcher applet, or download updates manually from the Matrix Games Product Download Page.

    Update files are cumulative, so you only need to download the most recent version. The development team regularly releases unofficial "Build XXX" updates with the latest fixes and improvements, which are fully supported.

??? info "FAQ: Where can I download more scenarios?"
    Command has 43 tutorials and 57 standalone scenarios included, but many more have been developed by the user community:

    - [Matrix Games Mods and Scenarios subforum](https://forums.matrixgames.com/viewforum.php?f=10233)
    - [Steam Workshop](https://steamcommunity.com/app/1076160/workshop/)
    - Community Scenario Pack (CSP) - regularly updated anthology of community scenarios

??? info "FAQ: Command crashed and I hadn't saved. Is my progress lost?"
    Command automatically saves your scenario every 20 seconds on a rotating series of autosave files. You can find them at:

    `[CMO install folder]\Scenarios\Autosaves\[Scenario Name]\Autosave_XXX.scen`

    Alternatively, restart Command and click "Resume from autosave" on the start screen to quickly load the most recent autosave.

Command Modern Operations is available through multiple distribution channels including Steam, Matrix Games, and physical retail. Installation varies slightly depending on your purchase method:

- **Steam**: Command will download and install automatically through the Steam client. Updates are handled automatically.
- **Matrix Games**: Download the installer from your Matrix Games account and run the setup executable. Register your product key when prompted.
- **Physical/DVD**: Insert the disc and follow the on-screen installation prompts. You may need to download updates separately after installation.

## 1.1 System Requirements

Minimum system requirements, with recommended requirements in
parentheses:

OS: 7 / 8 / 10 *(since version 1.05, Windows 7 is not supported)*

CPU: Any multi-core CPU; Quad-core CPU and above recommended

RAM: 4 GB (8GB+ recommended)

Video/Graphics: DirectX 9.0c compatible video card with 128 MB RAM
*(since version 1.05, DX11 is STRONGLY recommended)*

Sound: Compatible sound card

Hard disk space: 40GB free minimum, actual used space likely to grow
with usage

DVD-ROM: Yes, for boxed version

DirectX version: DirectX 9.0c (Suitable Direct-X version bundled with
game) *(since version 1.05, DX11 is STRONGLY recommended)*

Note: Large scenarios with many "moving parts" will run slower on the
same computer than smaller ones.

Note: Prior to 1.05 2GB RAM was the minimum requirement.

## 1.2 Support

The quickest way to get responses from members of either the COMMAND
development team or the simulation community is to:

· Register as a new user of the forum at matrix games forums
(<http://www.matrixgames.com/forums/>).

· Log in, and find the Command support area.

· (Optionally) Do a quick search for previous posts and threads on
keywords best reflecting your problem. The "bug" might turn out to be a
by-design gameplay element or have been already found and fixed.

· Start a new thread with a meaningful name and (optionally) a quick
reference to an unsuccessful search for "prior art". As a minimum,
please specify the version of COMMAND you are running and the scenario
(if there are any problems with gameplay), and the mode of play.

· Should a bug be reported, a save game file of the bug in 'action' is
***absolutely necessary***. COMMAND is an incredibly complex simulator,
and thus a save is needed to be able to reproduce the bug and provide
ways to fix it.

· Wait for replies.

· What to do when editing a scenario: If you need assistance editing a
scenario there are resources that will help. We hope this manual will be
a primary resource, but we do expect to see questions and posts on our
support forums which the developers will monitor along with experienced
players.

## 1.3 Notes for Multitaskers and Returning Players

- COMMAND does not automatically pause when you switch to other
  applications. The message popup will still occur for those messages
  set to popup as requested in the Game Options menu.

- COMMAND has undergone many changes from version 1.0 in September 2013
  to the present. For a detailed list of each and every change, see
  **14.0 COMMAND Update History** on page
  [350](#command-update-history).

- As of version 1.3, if the computer goes to sleep while COMMAND is
  running, it will wake up with COMMAND running.

- Different scenarios can have vastly different performance on the same
  computer. Scenario editors should be encouraged to limit the number of
  "moving parts", such as units not set to "blind", satellites, or units
  in general.

