from collections import Counter


class Hand:
    def __init__(self, cards, bid):
        self.cards = [*cards]
        self.bid = int(bid)
        self.determine_type_2()

    def determine_type_2(self):
        if self.cards == [*"JJJJJ"]:
            self.type = "FiveKind"
            return

        counting = Counter(cards)
        values = counting.values()
        jokers = counting["J"]

        print()
        print(counting)
        most, most_count = counting.most_common()[0]
        if most == "J":
            most, most_count = counting.most_common()[1]
        print(most)
        counting[most] += jokers
        del counting["J"]
        values = counting.values()
        print(counting)

        if 5 in values:
            self.type = "FiveKind"
        elif 4 in values:
            self.type = "FourKind"
        elif 3 in values and 2 in values:
            self.type = "FullHouse"
        elif 3 in values:
            self.type = "ThreeKind"
        elif 2 in values and len(values) == 3:
            self.type = "TwoPair"
        elif 2 in values:
            self.type = "OnePair"
        elif len(values) == 5:
            self.type = "HighCard"
        else:
            raise Exception("NO TYPE")

    def determine_type(self):
        counting = Counter(self.cards)
        if 5 in counting.values():
            self.type = "FiveKind"
        elif 4 in counting.values():
            self.type = "FourKind"
        elif 3 in counting.values() and 2 in counting.values():
            self.type = "FullHouse"
        elif 3 in counting.values():
            self.type = "ThreeKind"
        elif 2 in counting.values() and len(counting) == 3:
            self.type = "TwoPair"
        elif 2 in counting.values():
            self.type = "OnePair"
        elif len(counting) == 5:
            self.type = "HighCard"
        else:
            raise Exception("NO TYPE")

    def __repr__(self):
        return "".join(self.cards)

    def __lt__(self, other):
        # letter_order = "AKQJT98765432"
        letter_order = "AKQT98765432J"
        type_order = [
            "FiveKind",
            "FourKind",
            "FullHouse",
            "ThreeKind",
            "TwoPair",
            "OnePair",
            "HighCard",
        ]
        if self.type == other.type:
            for i in range(5):
                if self.cards[i] == other.cards[i]:
                    continue
                else:
                    return letter_order.index(self.cards[i]) > letter_order.index(
                        other.cards[i]
                    )
        else:
            return type_order.index(self.type) > type_order.index(other.type)
        raise ("ERROR")


hands = []
for line in open("advent7.txt"):
    cards, bid = line.split(" ")
    print(cards)
    hand = Hand(cards, bid)
    hands.append(hand)

    print(hand, hand.type, hand.bid)

som = 0
for i, hand in enumerate(sorted(hands)):
    print(i + 1, hand, hand.type, hand.bid)
    som += (i + 1) * hand.bid

print(som)
