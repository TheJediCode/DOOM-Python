import time
import random

items = []
neighbor = random.choice(["Carmack", "John", "Romero"])


def print_p(message):
    print(message)
    time.sleep(2)


def play_again():
    response = valid_input("\n\nPlay again? " "Yes or no\n", "yes", "no")
    if "yes" in response:
        game()


def valid_input(prompt, option1, option2):
    while True:
        choice = input(prompt).lower()
        if option1 in choice:
            break
        elif option2 in choice:
            break
        else:
            print("Please choose a valid option.")
    return choice


def invalid_input():
    print_p("Please enter a valid response.")


def intro():
    print_p("\nYou have entered into a doomed world of Hell on Earth.")
    print_p("Alone in your house, the end of days rages outside.")
    print_p("Hordes of demons roam the streets, hunting for their prey.")
    print_p("Your pet rabbit, Daisy, has been killed.")
    print_p("Will you be their next prey?")


def go_outside():
    time.sleep(2)
    print_p("""\nLooking around your home, you see a pile of wood and some
food.\n""")
    print_p("Neither will last long.")
    print_p("\nDo you go outside to look for supplies or do you stay at home?")
    choice = valid_input("\nGo outside or stay here?\n\n", "outside", "here")
    if "outside" in choice:
        store_or_gas()
    elif "here" in choice:
        fortify_or_eat()


def store_or_gas():
    print_p("\nCautiously, you exit the safety of your home.")
    print_p("""Greeted by reddened and blackened skies with howling wind and
the smell of fetid flesh, you scarcely recognize the world before
you.""")
    print_p("""But supplies are needed. There is a gas station a block away,
but there's a full superstore about a mile in the opposite
direction.""")
    choice = valid_input("\nGas station or superstore?\n\n", "gas", "store")
    if "store" in choice:
        chainsaw_or_gun()
    elif "gas" in choice:
        gas_attack()


def gas_attack():
    print_p("""\nYou make it to the gas station in little time,
but the echoes of demonic screaming are
growing in strength.""")
    print_p("""Suppressing the oncoming panic in your heart,
you push open the door to gas station -- once a staple
of your morning routine, now a dystopian hellscape dreamt of only
by the depraved.""")
    print_p("""With scarce choices, you grab a few snacks,
the only items left to consume in the barren station.""")
    print_p("""But no sooner are your pockets filled than does
a four legged beast, ripped from the mythos of demonology,
shatter through the glass doors.""")
    choice = valid_input("\nRun or fight?\n\n", "run", "fight")
    if "run" in choice:
        gas_run_death()
    elif "fight" in choice:
        gas_fight_death()


def gas_run_death():
    print_p("""\nYour legs pound against the tile floor, desperately attempting
to escape the unholy monster barreling after you.""")
    print_p("But without having eaten today, you lose stamina quickly.")
    print_p("""In a matter of moments, the creature ensnares you, pinning your
body to the floor as it rips and tears away your flesh,""")
    print_p("your screams deafening, but fall to a deaf God's ears.")
    play_again()


def gas_fight_death():
    print_p("\nGrabbing anything you can, you hurl it at the demon.")
    print_p("""But with no true weapon, your effete attacks scarcely damage the
horror.""")
    print_p("""In a matter of moments, the creature ensnares you,
pinning your body to the floor as it rips and tears "
away your flesh,""")
    print_p("your screams deafening, but fall to a deaf God's ears.")
    play_again()


def chainsaw_or_gun():
    print_p("""\nFighting through the terror choking your heart,
you make your way to the superstore.""")
    print_p("The sounds of demonic lurking horrors perturb your ears.")
    print_p("""Quickly grabbing a few canned goods, you decide to search
the hunting and hardware section of the store.""")
    print_p("""Here you find both an chainsaw and a gun.
But you can only take one.""")
    choice = valid_input("\nChainsaw or gun?\n\n", "chainsaw", "gun")
    if "chainsaw" in choice:
        items.append(["chainsaw"])
        store_demon_chainsaw()
    elif "gun" in choice:
        items.append(["gun"])
        store_demon_gun()


def store_demon_gun():
    print_p("""\nGrabbing the pistol and loading it up,
you feel prepared to fight.""")
    print_p("""But that preparedness is quickly tested as an undead
humanoid creature steps forward, its skin all but rotten.""")
    print_p("You empty the clip into the monster, but it does little damage.")
    print_p("""Out of ammo and defenseless, the horror sinks its nails
into your flesh and rips your skin. Driving its teeth
into your neck, the last thing you feel before your
life goes dark is the pain of your throat being
ripped from your body.""")
    play_again()


def store_demon_chainsaw():
    print_p("""\nSuddenly from the corner comes a humanoid creature, all but
skinless and rotten.""")
    print_p("""Its putrid odor assaults your senses as it lets out a
horrifying screech.""")
    print_p("But you're prepared for the undead.")
    print_p("""With one strong swing, you slam the chainsaw into the
undead's skull, splitting it in half and incapacitating the creature.""")
    print_p("""You're not sure that it's dead, or if the dead can die,
but it has stopped moving. Now you must decide whether to gather
more fortification supplies or to use what you have at home.""")
    choice = valid_input("\nGet supplies or go home?\n\n", "supplies", "home")
    if "supplies" in choice:
        items.append(["wood", "food"])
        store_wood_go_home()
    elif "home" in choice:
        store_go_home_death()


def store_go_home_death():
    print_p("""\nYou hurry out of the store and run back home,
quickly boarding up your door again.""")
    print_p("""But you realize there isn't enough wood. Too much
of it has already been damaged.""")
    print_p("""With a well of dread within your heart, you brace
yourself to go back outside.""")
    print_p("""But the moment you open the door, a horned beast with
eyes of fire, waiting for you -- its prey -- to step out, gores
you with its massive spike.""")
    print_p("""Though you swing your chainsaw on it, it is already
too late. Bleeding to death, you lie next to your life-taker,
the demon; it, too, bleeding from its wound.""")
    print_p("And the world goes darker than black.")
    play_again()


def store_wood_go_home():
    print_p("""\nHurriedly, you gather as many bits of wood as you
can from the store, then rush back outside as you hear the
noise of the undead returning to life.""")
    print_p("""With a weapon, wood, and food, you run to your house
and prepare for the next attack.""")
    choice = valid_input("\nFortify first or eat first?\n\n", "fortify", "eat")
    if "fortify" in choice:
        home_low_energy()
    elif "eat" in choice:
        home_no_defense()


def home_no_defense():
    print_p("""\nAs you consume your food, quickly and quietly, a faint
rustling outside pulls your attention away.""")
    print_p("""Food still in hand, you approach the window to see if
something is out there.""")
    print_p("""But, to your great relief, it seems to be only the wind.
You turn away from the window and resume eating, deciding you will
board up the window once you've eaten.""")
    print_p("""But a hellish predator crashes through the window, landing
on your back and sinking its talons into your shoulders.""")
    print_p("""As it rips and tears your flesh, death becomes an invitation
-- the only escape from this surreal hell.""")
    play_again()


def home_low_energy():
    print_p("""With your house fortified, the windows boarded, and your
chainsaw at your side, you must now decide what to do with your food.""")
    print_p("""You don't feel like you're starving, but you're definitely
low on energy. Despite this, it's tempting to save as much food
as you can.""")
    choice = valid_input("\nDo you eat or do you fast?\n\n", "eat", "fast")
    if "eat" in choice:
        demon_finale_chainsaw()
    elif "fast" in choice:
        hunger_death()


def hunger_death():
    print_p("""\nDeciding to save your food, you sit and wait near
the door, chainsaw in hand.""")
    print_p("""Hours pass. In your low energy state, you find yourself
drifting into unconsciousness.""")
    print_p("""But a crash through door rips you back to reality. A
four legged demon, bearing horns as large and sharp as swords,
stares you in the face.""")
    print_p("""You swing your chainsaw, but you find your arms
failing you as your body suddenly becomes weak.""")
    print_p("""Missing your swing, the demon seizes its opportunity
and snatches you in its powerful jaw, crushing your bones with
its jagged teeth, like rocks justting from an ocean alcove.""")
    print_p("""The light is sapped from your eyes as your body, in
unmitigable pain, shuts down, and the world -- your world --
becomes darker than black.""")
    play_again()


def demon_finale_chainsaw():
    print_p("""\nRested, vigilant, and ready to rip and tear, you sit
by the door and wait.""")
    print_p("""After over an hour of watching, waiting, you hear finally
hear a noise at the door.""")
    print_p("""The creatures claw and tear. You know the door won't
last forever.""")
    choice = valid_input("\nStand and fight or run?\n\n", "fight", "run")
    if "fight" in choice:
        demon_finale_chainsaw_win()
    elif "run" in choice:
        demon_finale_chainsaw_lose()


def demon_finale_chainsaw_win():
    print_p("""\nAs the demons break through the door, you immediately
swing your chainsaw.""")
    print_p("""Your weapon rips through hellspawns, rendering them into
piles of soft mush, punishing them for hurting your little rabbit.""")
    print_p("""As the bodies stack on top of each other, the demons begin
to flee, now terrified of your awesome presence.""")
    print_p("""With your enemies running, tails between their legs, you
stand atop the vanquished and let out a blood-curdling battlecry.""")
    print_p("You are the Doom Slayer.")
    play_again()


def demon_finale_chainsaw_lose():
    print_p("\nRunning like a coward, you lock yourself in the bathroom.")
    print_p("""In a matter of moments, your home is breached. The
onslaught of demons make short work of your bathroom door.""")
    print_p("""As they rush into the room, you are overwhelmed. Horns
pierce your skin and teeth crush your bones.""")
    print_p("""The world hears your final utterances of pain, deafening
cries that fall upon the ears of a deaf God. You have died.""")
    play_again()


def fortify_or_eat():
    print_p("""\nChoosing to stay where it's familiar, though questionably
safe, you decide to remain home.""")
    print_p("""Hunger strikes you, but you know you have only a limited
time to fortify your home.""")
    choice = valid_input("\nDo you fortify or eat?\n\n", "fortify", "eat")
    if "fortify" in choice:
        fortify_home_hunger()
    elif "eat" in choice:
        eat_first()


def fortify_home_hunger():
    print_p("""\nYou board up the windows and the door, but your hunger
is palpable. You feel low on energy, but you also want to conserve
what little food you have.""")
    choice = valid_input("\nSave your food or eat it?\n\n", "save", "eat")
    if "save" in choice:
        hungry_home_death()
    elif "eat" in choice:
        full_home_attack()


def hungry_home_death():
    print_p("""\nDeciding to save your food, you hide in a dark corner
of your home, hoping the creatures outside don't make you their meal.""")
    print_p("""But as your body tries to conserve energy, you find yourself
falling asleep...""")
    print_p("""Only to be seized from your sleep by a crash through the
door. A monstrous four legged beast stands before you.""")
    print_p("""With no energy to run or fight, you become easy prey to
the ungodly abomination.""")
    print_p("""With terrified cries af agony, you are torn asunder by
the invading evil. The world goes black.""")
    play_again()


def full_home_attack():
    print_p("""\nFeeling rejuvinated, you vigilantly sit by the door,
like a sentinel waiting for danger.""")
    print_p("After a while, that danger finally comes.")
    print_p("""The sounds of some unimaginable abomination tearing at
your door pervades your home. You feel strong enough to either fight
the demon with your last bit of wood, or abandon your house and make
a run for it.""")
    choice = valid_input("\nDo you run or fight?\n\n", "run", "fight")
    if "fight" in choice:
        full_home_attack_death()
    elif "run" in choice:
        full_home_attack_run()


def full_home_attack_death():
    print_p("\nFeeling bold, and perhaps stupid, you stand your ground.")
    print_p("""The demon bursts through your door, turning it into a pile
of splinters.""")
    print_p("""With a fierce swing, you hit the monster as hard as you
possibly can, breaking the bit of wood.""")
    print_p("But you do no more damage to it than a fly could do to you.")
    print_p("""Gruelingly, the horned beast rips and tears you apart,
devouring your flesh as your world fades to darkness.""")
    play_again()


def full_home_attack_run():
    print_p("""\nKnowing you are outmatched, you sneak through the
kitchen window and run out the back of your home, no longer a
haven of safety but a hub of certain death.""")
    print_p("""Without a weapon or supplies, you're left exposed to
the dark world you now inhabit.""")
    print_p("""You must go somewhere. There is a superstore a mile
or so away from you, but you could also take shelter in your neighbor's
abandoned home.""")
    choice = valid_input("\nStore or neighbor's house?\n\n", "store", "neighb")
    if "store" in choice:
        store_noweap_death()
    elif "neighb" in choice:
        neighbor1()


def store_noweap_death():
    print_p("""\nLike a newborn thrust into the world and abandoned
by its parents, God has abandoned you.""")
    print_p("""Defenselss, you try to make your way to the store,
but you're scarcely up the road before the demon -- who has
realized you're no longer home -- charges after you.""")
    print_p("""Unable to outrun it, the beast gores you from behind,
tearing out your spine and crushing your bones.""")
    print_p("""Death comes instantaneously for the lucky ones; you
are not one of them.""")
    play_again()


def neighbor1():
    print_p("""\nSneaking into your neighbor's house, unnoticed by
the demons, you look around.""")
    print_p("""There may be food in the kitchen, but you remember
that your neighbor, """ + neighbor + """, was a gun lover. There might
be a weapon in his study.""")
    choice = valid_input("\nKitchen or study?\n\n", "kitchen", "study")
    if "kitchen" in choice:
        neighbor1_kitchen_death()
    elif "study" in choice:
        neighbor1_study()


def neighbor1_kitchen_death():
    print_p("\nUnarmed, you go to " + neighbor + "'s kitchen.")
    print_p("""As you root through the cabinets, all but empty, you
hear a noise behind you.""")
    print_p("""Looking through the kitchen window to your own abandoned
home, you witness a sight that is cause for sheer panic:""")
    print_p("""The demons have left.""")
    print_p("""And just as you realize that fact, a horrendous creature,
walking on powerful hooves, steps into the kitchen.""")
    print_p("""Defenseless, you try to run for the exit. But the swift
abomination catches you effortlessly, gnawing your leg into an
unrecognizable hunk of flesh.""")
    print_p("""Lying on the floor, bleeding, you pray to God for the
torture to end. And God subsequently grants your wish as the
world falls into blackness.""")
    play_again()


def neighbor1_study():
    items.append(["shotgun"])
    print_p("\nHeading into " + neighbor + """'s study, you see in a glass
case his most prized weapon:""")
    print_p("A double-barreled shotgun.")
    print_p("""Taking the weapon and loading it, you're ready to take on
Hell's armies on your own terms.""")
    print_p("""You head to the kitchen in search of provisions, but find
a spawn of Hell standing to challenge you.""")
    choice = valid_input("\nDo you fight or do you run?\n\n", "fight", "run")
    if "fight" in choice:
        neighbor1_win()
    elif "run" in choice:
        neighbor1_lose()


def neighbor1_lose():
    print_p("""\nYou run away like a frightened child, dropping the
powerful weapon from your hands.""")
    print_p("""But the demonic predator is faster than your weak little
legs. It pounces on you, tearing you limb from limb.""")
    print_p("There you die, becoming the creature's next meal.")
    play_again()


def neighbor1_win():
    print_p("""\nLocking eyes with the demon, realizing the badass that
you really are, you raise your weapon against the unholy one.""")
    print_p("The beast charges you. But you were born for this.")
    print_p("""With a lithe sidestep, you get the drop on the four
legged beast. Your finger squeezes the trigger and launches a blast
of shrapnel into the demon's back.""")
    print_p("""As it shrieks in pain, you relod the weapon and fire again,
erasing the place where its head used to be. They killed your pet
rabbit. They deserve no mercy.""")
    print_p("""Dragging the corpse outside for its cohorts to see,
you make one thing clear:""")
    print_p("""You're not stuck in Hell with these demons.
They're stuck in Hell with you.
You are the Doom Slayer.""")
    play_again()


def eat_first():
    print_p("""\nFeeling replenished, but now out of food, you realize
you need to either board up your home now and get supplies tomorrow
-- risking the night with no weapon -- or venture out to procure
more food and something to defend yourself with.""")
    choice = valid_input("\nGo outside or fortify home?\n\n", "out", "fort")
    if "out" in choice:
        go_outside_2()
    elif "fort" in choice:
        eat_first_die_later()


def eat_first_die_later():
    print_p("""\nAs you begin nailing bits of wood over the door, you hear
an ominous scraping.""")
    print_p("""But you can't tell where it's coming from. It sounds like
maybe the roof.""")
    print_p("You look out the window, but see nothing.")
    print_p("You return to boarding up your door --")
    print_p("""until, with a blood curdling screech, a winged hell-beast
shatters the window, sinking its talons into your ribs as it lands.""")
    print_p("""The agony you feel is incomparable to any earthly pain.
You let out a deafening scream, but it only falls upon God's deaf ears.""")
    print_p("""In a matter of moments, the winged beast rips the soul
from your body.""")
    play_again()


def go_outside_2():
    print_p("""\nStepping into the hazy realm of Hell surrounding what was
once a tranquil neighborhood, fear grips you.""")
    print_p("""You know there will be supplies at the local superstore,
but that's a long walk.""")
    print_p("You also remember that your neighbor, " + neighbor + """,
was a gun collector. You're more likely to find a weapon next door,
but unlikely to find food.""")
    choice = valid_input("\nStore or neighbor's house?\n\n", "store", "neighb")
    if "store" in choice:
        store_2_death()
    elif "neighb" in choice:
        neighbor2()


def store_2_death():
    print_p("""\nWandering down the street, weaponless and defenseless,
you realize you may have made a mistake.""")
    print_p("""The unearthly howl of some unimaginable horror chills your
bones.""")
    print_p("The howling gets closer.")
    print_p("Your brisk walk turns into a jog.")
    print_p("""As the sound of horse-like footsteps behind you grows louder,
your jog turns into a sprint.""")
    print_p("""And as you sprint, your heart pounding like a frightened,
trapped animal, the demon catches you from behind.""")
    print_p("""You pray for a quick death, but the prayer is met only by the
sound of a hungry monster ripping the flesh from your bone.""")
    play_again()


def neighbor2():
    print_p("""\nBreaking into your neighbor's house, hoping not to be
noticed by the monsters surrounding your own home, you quietly
creep inside.""")
    print_p("""You're not hungry, but you realize you are out of food.
There might be some in the kitchen.""")
    print_p("""But you also know that if you're attacked, you'll be
defenseless. Maybe you should check the study for a weapon first.""")
    choice = valid_input("\nKitchen or the study?\n\n", "kitchen", "study")
    if "kitchen" in choice:
        neighbor2_kitchen_death()
    elif "study" in choice:
        neighbor2_study()


def neighbor2_kitchen_death():
    print_p("""\nFoolishly, you enter the kitchen first, despite being
both full and defenseless.""")
    print_p("""After looking through a few cabinets, you find very little
edible food. You turn around to head to the study.""")
    print_p("""But a monstrous, four legged beast with horns like giant
daggers stares at you from the doorway.""")
    print_p("Frozen in place, you can do little but accept your fate.")
    print_p("""After what feels like minutes pass, you move ever so slightly
toward a knife lying out on the kitchen counter.""")
    print_p("""But the demon is swift, and in the blink of an eye it lunges
at you, breaking your bones with its heavy hooves, mauling you into
an unrecognizable pulp of human parts.""")
    print_p("At least it was a quick death.")
    play_again()


def neighbor2_study():
    items.append(["shotgun"])
    print_p(" ")
    print_p("Entering " + neighbor + "'s study, you find his crowning jewel:")
    print_p("The double-barreled shotgun.")
    print_p("""You take it and a box of shells, ready to send Hell back to
where it came from.""")
    print_p("""Heading to the kitchen, you decide now is a good time to
search for provisions.""")
    neighbor2_kitchen_finale()


def neighbor2_kitchen_finale():
    print_p("""\nStepping into the kitchen, you find yourself face to face
with not one -- not two -- but almost half a dozen horrendous creatures.""")
    print_p("""Pus oozing from their fetid, decaying bodies, horns atop
their heads and fire in their eyes.""")
    print_p("They've been waiting for you -- their dinner.")
    print_p("It's do or die time.")
    choice = valid_input("\nDo you run or fight?\n\n", "fight", "run")
    if "run" in choice:
        neighbor2_kitchen_finale_death()
    elif "fight" in choice:
        neighbor2_kitchen_finale_win()


def neighbor2_kitchen_finale_death():
    print_p("""\nLike the coward you are, you drop your weapon and run,
urinating in your pants while you do so.""")
    print_p("""The demons let out gutteral, bizarre laughs.""")
    print_p("But only for a moment.")
    print_p("""In the next intant, all of the creatures descend upon you,
ripping and tearing your flesh until nothing left of your cowardly
life remains.""")
    play_again()


def neighbor2_kitchen_finale_win():
    print_p("\nHell hath no fury like a slayer scorned;")
    print_p("""These abominations took your home from you and killed
your rabbit and now it's time to pay.""")
    print_p("""You pull the trigger, unleashing a powerful blast from
the shotgun, obliterating two of ungodly beings. With a quick
sidestep, you reload and blast two more of the beasts.""")
    print_p("""The last of the undead horrors turns its tail and runs
in fear of you, but you show it the same mercy it showed
Daisy the rabbit.""")
    print_p("""A powerful spray of shotgun shrapnel erases the monster's
head. Triumphant, you drag the body of the beasts into a pile
outside, a warning to anything else that might think about preying
on you.""")
    print_p("""Standing atop the demonic cadavers, you let out a fierce
battlecry.""")
    print_p("You are the Doom Slayer.")
    play_again()


def game():
    intro()
    go_outside()


game()
