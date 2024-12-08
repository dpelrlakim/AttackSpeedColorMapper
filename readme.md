# Attack Speed Color Mapper (ASCM)


Important: The overlay window is small and designed to stay out of the way. However, **accidentally clicking on it will cause you to miss that click**, so be cautious during gameplay.

### This program helps you optimize attacks in League of Legends.

In League of Legends (LoL), "Attack Speed" (AS) is defined as the number of basic attacks a champion can perform in 1 second. This value has units of *attacks per second*. Each player will control one *champion*, and each champion can use *basic attacks*. Basic attacks have a cooldown, which is just the reciprocal of AS. As such, hitting an enemy with a basic attack, then moving your champion until your next basic attack is ready, is the most optimal way to fight in LoL.

In particular, movement between attacks is often used to make distance from enemies. The common pattern of ( attacking --> walking away --> attacking --> walking away --> ... ) is called **kiting**.

### The Problem: Not only is the AS value written in a very small font, **it is difficult to gain a sense of how much to wait between attacks**. 

As an example, let's consider the following scenario. A champion with 1.25 AS is technically at a disadvantage against a champion with 1.50 AS. If the player does not have a good sense of his own AS, then he may waste precious time and miss his timing for his next attack. This is often a matter of skill, but sometimes context matters. For example, he could have originally had 1.25 AS, but buying an item increased it to 1.50 and he may not have looked at his new attack speed.

ASCM is a program that reads the AS value on the screen for you, and tells you its value as a **specific color** (and also numerically in a larger font). For example, at 0.7 AS, your indicator will be green, but at 2.5 AS, your indicator will be red. Since colors can be interpreted without focusing one's eyes on it, this will cut down the player's time to calculate how much to wait between attacks. Color is also easier to understand (rainbow spectrum) as opposed to the unnormalized scale of ~0.6-2.5+ AS that other players will use.

The more the player gets familiar with this indicator, the more they will be used to the color scheme and he will soon be able to get the kiting timing down almost perfectly.

Important: It is a small window, and mostly out of the way. But once again, **the game will not recognize clicks on top of the overlay window.** 

### Benefits & incentives for advanced players:

As more experienced players know, a champion's AS will change pretty unpredictably within a teamfight. In a teamfight, up to 10 champions are involved, and each champion (self, allies and enemies) has their own abilities and items that can influence your attack speed. **It is usually impossibly difficult as a human to keep track of this highly fluctuational value while also keeping his own champion safe in a teamfight.** Pro LoL players typically have an empirically developed sense in optimizing their kiting, and they mentally keep track of team composition and each champion's item composition at all times. This is an extremely difficult skill to master for most non-pro LoL players and will require years of practicing, but this kind of player-level optimization is required in competitive gameplay. Using ASCM will drastically help with this **fluctuating AS issue**, even for casual players. 

ASCM updates its indicator colour once every 30 ms (~33 updates/s). This means that it picks up on champion AS changes pretty fast. Combined with the fact that color is an intuitively ingestible form of data, without even having to directly look at the overlay. This is often enough to change the outcome of the teamfight, which is sometimes enough to change the outcome of the entire match.

There are many steps to perfect kiting other than timing your attacks. However, timing is still a critial part of it, and ASCM can be a valuable tool to achieve mastery in this area of kiting.

### Multi-monitor guide

NOTE: If you have a multi-monitor setup, the following monitors MUST be pointing to the same screen:
* The monitor that the **LoL game client is running on** (the monitor that you play the game on)
* The monitor that is the **main display** recognized by the Windows OS

### Resolution modes guide

Upon starting the program, it will ask the user to choose a mode. The user MUST choose the correct mode, otherwise ASCM will look at a different part of the screen and will not work.

Choose the mode that matches the resolution of the LoL monitor.

Example: If you're running LoL on a laptop with a 1920x1080 screen, choose the mode for 1920x1080 (FHD).

### Read & write box guide

Definitions:
* A **box**, in this context, is a rectangular area of the screen that is expressed by a coordinate pair of the rectangle's vertex closest to the origin, and the width and the height of the rectangle.
* A **read box** is a box that is meant to read the AS value on your screen. You likely need to (and are encouraged to) manually adjust the parameters for the box object based on your screen.
* A **write box** is a box that you will see the AS color out of. This can be wherever on the screen you want. Its size can also be customized. However, it should be out of the way of your clicking as that area will not be clickable, but still visible enough for your eyes to pick up during a hectic teamfight.

### This program does not read any LoL data from memory.

All it does is taking a screenshot of your attack speed data every 30 ms, using OCR (Optical Character Recognition) to read its value, and outputting it as a certain color. Since it does not interact with any LoL data in memory, **you cannot be banned for using ASCM**.
