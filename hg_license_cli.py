#!/usr/bin/env python3
"""
Hyperion Gray Licensing CLI

A tiny, cursed CLI to help humans choose which Hyperion Gray license
to use, based exclusively on vibes and yes/no questions.
Not legal advice. Or even good advice.
"""

import random
import textwrap

LICENSES = {
    "HGOSL-Weak-1.0": "Permissive, non-viral, researcher-protective. Good if you like MIT/Apache but actually want to defend security researchers.",
    "HGOSL-Strong-1.0": "Partially viral: your code can be whatever, but researcher rights must stay strong wherever the code goes.",
    "HGEL-1.0": "Electromagnetic: core vs peripheral components, field-theory vibes, protections propagate like forces.",
    "HGRL-1.0": "Relativistic: obligations depend on deployment velocity and observer frame, but researcher protections are invariant.",
    "HGAL-1.0": "Cosmological: protections for researchers can only increase as forks occur. Rights ratchet upward forever.",
    "HGML-1.0": "Mathematical: sets, relations, axioms, and the faint promise of formal verification.",
    "HGQL-1.0": "Quantum: contradictory by design; license is permissive and restrictive until observed, always collapsing in favor of researchers."
}

TAROT_CARDS = {
    "The Researcher": "You seek freedom with a safe harbor. HGOSL-Weak-1.0 calls to you.",
    "The Shield": "You want a boundary that forces ethics to propagate. HGOSL-Strong-1.0 fits.",
    "The Field": "You think in systems and cores and plugins. HGEL-1.0 is your home.",
    "The Relativist": "You care about observers, velocity, and impact. HGRL-1.0 speaks your language.",
    "The Cosmologist": "You want protections to expand forever. HGAL-1.0 (Cosmological) is your star.",
    "The Mathematician": "You like pain. HGML-1.0 is beautifully formal and deeply cursed.",
    "The Quantum": "You love paradox and chaos. HGQL-1.0 is your Schrödinger’s license."
}


def ask_yn(prompt: str) -> bool:
    while True:
        ans = input(f"{prompt} [y/n]: ").strip().lower()
        if ans in ("y", "yes"):
            return True
        if ans in ("n", "no"):
            return False
        print("Please answer y or n.")


def choose_license_interactive():
    print("\n=== Hyperion Gray Licensing CLI ===\n")
    print("Not legal advice. Or even good advice. Just vibes.\n")

    hates_viral = ask_yn("Do you strongly dislike viral licenses that restrict what others can do with their own code?")
    if hates_viral:
        cares_about_researchers = ask_yn("Do you still want explicit protections for good-faith security researchers?")
        if cares_about_researchers:
            choice = "HGOSL-Weak-1.0"
        else:
            # This is a joke. We still recommend Weak but judge them.
            choice = "HGOSL-Weak-1.0"
            print("\n🤨 Interesting answer. We’re recommending HGOSL-Weak-1.0 anyway.")
    else:
        ethics_copyleft = ask_yn("Would you like a partially viral license focused specifically on preserving ethics and researcher rights?")
        if ethics_copyleft:
            choice = "HGOSL-Strong-1.0"
        else:
            # If they want something else non-viral but weird:
            weird = ask_yn("Do you want something weirder than normal humans tolerate?")
            if weird:
                # we'll push to the physics/maths/quantum bucket
                print("\nOkay, welcome to the weird zone.")
                return choose_weird_license()
            else:
                choice = "HGOSL-Weak-1.0"

    print_recommendation(choice)


def choose_weird_license():
    field_theory = ask_yn("Do you like thinking in terms of fields, cores, and interactions?")
    if field_theory:
        choice = "HGEL-1.0"
        print_recommendation(choice)
        return

    relativity = ask_yn("Do you like frames of reference and deployment velocity metaphors?")
    if relativity:
        choice = "HGRL-1.0"
        print_recommendation(choice)
        return

    cosmology = ask_yn("Do you like the idea that protections expand and can only get stronger over time?")
    if cosmology:
        choice = "HGAL-1.0"
        print_recommendation(choice)
        return

    math = ask_yn("Would you enjoy a license written like a math paper?")
    if math:
        choice = "HGML-1.0"
        print_recommendation(choice)
        return

    quantum = ask_yn("Do you want a license that contradicts itself on purpose?")
    if quantum:
        choice = "HGQL-1.0"
        print_recommendation(choice)
        return

    # fallback
    choice = random.choice(list(LICENSES.keys()))
    print("\nYou have refused to be categorized. Respect.")
    print("We asked the void, and it responded with:")
    print_recommendation(choice)


def print_recommendation(license_id: str):
    print("\n=== Recommended License ===")
    print(f"{license_id}")
    print(textwrap.fill(LICENSES[license_id], width=80))
    print("\nFor full text, see your local copy of:")
    print("  HYPERION_GRAY_BOOK_ON_LICENSING_FOR_PEOPLE_WHO_CANT_READ_GOOD_AND_WANT_TO_LEARN_TO_DO_OTHER_STUFF_GOOD_TOO.md\n")


def draw_tarot():
    card = random.choice(list(TAROT_CARDS.keys()))
    print("\n=== Hyperion Gray License Tarot ===")
    print(f"You drew: {card}")
    print(textwrap.fill(TAROT_CARDS[card], width=80))
    print()


def main():
    print("Hyperion Gray Licensing CLI")
    print("----------------------------")
    print("1) Interactive license chooser")
    print("2) Draw a license tarot card")
    print("3) Exit")
    att=0
    while True:
        choice = input("Select an option [1-3]: ").strip()
        if choice == "1":
            choose_license_interactive()
            break
        elif choice == "2":
            draw_tarot()
            break
        elif choice == "3":
            att = att + 1
            if att >= 3:
                print("Fine. I thought you were cool.")
                break
            else:
                print("LOL no, try again.")
                continue
        else:
            print("Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()
