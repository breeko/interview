class OnlyOne:
    # private class
    class __OnlyOne:
        def __init__(self, arg):
            self.arg = arg
        
        # string representation
        def __str__(self):
            return repr(self) + self.val
    
    # class variable
    instance = None
    
    def __init__(self, arg):
        if OnlyOne.instance is None:
            OnlyOne.instance = OnlyOne.__OnlyOne(arg)
        else:
            OnlyOne.instance.arg = arg
    
    def __getattr__(self, name):
        return getattr(self.instance, name)

class Card:
	suit_mapping = {1: 'C', 2: 'D', 3: 'H', 4:'S'}
	num_mapping = dict([(i,str(i)) for i in range(1,11)] + [(11, 'J'), (12, 'Q'), (13, 'K'), (14, 'A')])
	def __init__(self, num, suit):
		assert suit in Card.suit_mapping
		assert num in Card.num_mapping
		self.num = num
		self.suit = suit

	def __eq__(self, other):
		return other.num == self.num and other.suit == self.suit

	def __lt__(self, other):
		if self.num != other.num:
			return self.num < other.num
		return self.suit < other.suit

	def __gt__(self, other):
		return not self < other

	def __le__(self, other):
		return self < other or self == other

	def __ge__(self, other):
		return self > other or self == other

	def __str__(self):
		return "%s%s" % (Card.num_mapping[self.num],Card.suit_mapping[self.suit])