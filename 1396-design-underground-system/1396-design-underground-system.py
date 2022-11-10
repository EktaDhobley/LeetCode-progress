# class UndergroundSystem:

#     def __init__(self):
#         #customerid : (timestart, startstation)
#         self.in = defaultdict(tuple)
        
#         #(start, end): timeend - timestart 
#         self.out = defaultdict(list)

#     def checkIn(self, id: int, stationName: str, t: int) -> None:
#         self.in[id] = (t, stationName)
        

#     def checkOut(self, id: int, stationName: str, t: int) -> None:
#         starttime, startstation = self.in[id]
#         total = t - starttime
#         #here stationname is end station
#         self.out[(startstation, stationName)].append(total)
        

#     def getAverageTime(self, startStation: str, endStation: str) -> float:
#         return sum(self.out[(startStation, endStation)]) / len(self.out[(self.startStation, self.endStation)])

class UndergroundSystem:
	def __init__(self):
		self.currentPassengers = defaultdict(tuple) # id -> (startStation, startTime)
		self.travelTimes = defaultdict(list) # stationStart:stationEnd -> [t1,t2]

	def checkIn(self, id: int, stationName: str, t: int) -> None:
		self.currentPassengers[id] = (stationName, t)

	def checkOut(self, id: int, stationName: str, t: int) -> None:
		startStation, startTime = self.currentPassengers.pop(id)
		self.travelTimes[f"{startStation}:{stationName}"].append(t - startTime)

	def getAverageTime(self, startStation: str, endStation: str) -> float:
		return mean(self.travelTimes[f"{startStation}:{endStation}"])
# # Your UndergroundSystem object will be instantiated and called as such:
# # obj = UndergroundSystem()
# # obj.checkIn(id,stationName,t)
# # obj.checkOut(id,stationName,t)
# # param_3 = obj.getAverageTime(startStation,endStation)