class TintedColors(object):
	def __init__(self,color):
		self.color = color
		self.hue = rgb_to_hsv(*color)[0]
	def tintedColor(saturation, value=1.0):
		def getColor(self):
			hsv = (self.hue,saturation,value)
			return hsv_to_rgb(*hsv)
		return property(getColor)
	
	gradientLeft=tintedColor(0.4)
	gradientRight=tintedColor(0.2)
	outlineColor = tintedColor(0.5)
	textColor = tintedColor(0.67, 0.6)
