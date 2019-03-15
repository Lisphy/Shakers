
import argparse

class shakes(object):
	def __init__(self):
	
		self.cmds = [
					'curl -X Get',
					]
		self.uris = [
					'uris://resource/',
					'http://resource/',
					'qury://resource/',
					]
		self.params = [
					'param1',
					'param2',
					'param3',
					]
		self.values = [
					'v1',
					'v2',
					'v3',
					'v4',
					'v5',
					]
		
		self.list = []
		
		self.prep = ''
		self.postp = '='
		
		self.prev = ''
		self.postv = ''
		
		self.seperate = '&'
		
		
	def do(self):
		self.clen = len(self.cmds)
		self.plen = len(self.params)
		self.vlen = len(self.values)
		
		aa = [ [int(x/(self.vlen**y)%self.vlen) for y in range(0, self.plen, 1) ] for x in range(0, self.vlen**self.plen, 1) ]
		
		for u in self.uris:
			for a in aa:
				mixed = u
				for i, v in enumerate(a):
					mixed +=  self.prep + str(self.params[i]) + self.postp + self.prev + str(self.values[v]) + self.postv
					if i + 1 < self.plen:
						mixed += self.seperate
				if self.clen:
					for c in self.cmds:
						self.list.append(str(c) + str(' ') + mixed)
				else:
					self.list.append(mixed)
				
		
	def showlist(self):
		for l in self.list:
		
			print(l)
		
		print(len(self.list))

if __name__ == '__main__':
	sh = shakes()
	parser = argparse.ArgumentParser(description='shakers value and param for uri. git - https://github.com/Lisphy/Shakers')
	parser.add_argument('values', metavar='values', type=str, nargs='+',
						help='multiplier values')
	parser.add_argument('--params', dest='params', type=str, nargs='+',
						default=['lisphy', 'SPI'],
						help='parameters ex: v1 v2 --params param1 param2 >> "param1=v1&param2=v1&..." ')
	parser.add_argument('--uris', dest='uris', type=str, nargs='+',
						default=['uris://spi.mobile/bf.do?','http://spi.mobile/bf.do?'],
						help='URIs ex: --uris https://my.com/api? >> "https://my.com/api?param1=v1&param2=v1&..." ')
	parser.add_argument('--cmds', dest='cmds', type=str, nargs='+',
						default=['get'],
						help='cmds ex: "curl -X Get/Post "')
	parser.add_argument('--prep', dest='prep', type=str,
						default='',
						help='pre-parameters ex: --params param --prep "my_" >> "my_param"')
	parser.add_argument('--postp', dest='postp', type=str,
						default='=',
						help='post-parameters ex: --params param --postp "_ize" >> "param_ize"')
	parser.add_argument('--prev', dest='prev', type=str,
						default='',
						help='pre-value ex: value1 value2 --prev "real_" >> "real_value1, real_value2"')
	parser.add_argument('--postv', dest='postv', type=str,
						default='',
						help='post-value ex: value1 value2 --postv "_xyz" >> "value1_xyz, value2_xyz"')
	parser.add_argument('--sep', dest='seperate', type=str,
						default='&',
						help='seperate-value ex: v1 v2 --param p1 p2 --sep "&" >> "p1=v1&p1=v2"')
						
	args = parser.parse_args()
	sh.values = args.values
	sh.params = args.params
	sh.uris = args.uris
	sh.cmds = args.cmds
	sh.prev = args.prev
	sh.postv = args.postv
	sh.prep = args.prep
	sh.postp = args.postp
	sh.seperate = args.seperate

	sh.do()
	sh.showlist()
