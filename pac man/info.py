global level,path,path2
		start=self.ghosts[0]
		end=self.pacman
		start2=self.ghosts[1]
		# end2=(random.choice(self.food))
		end2=(self.pacman[0],self.pacman[1]-4)

		cost=1
		prev_path=path
		prev_path2=path2
		  #try excepting to quick code boundary conditions and end of game scenes
		try:
			path=search(level,cost, start, end,10,True)
			
			path2=search(level,cost, start2, end2,10,True)
			if path==None :
				prev_path.pop(0)
				path=prev_path
			if path2==None:
				prev_path2.pop(0)
				path2=prev_path2

			move=path[1]
			move2=path2[1]
			self.ghosts[0]=move
			self.ghosts[1]=move2
		except:
			pass


