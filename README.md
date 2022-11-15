
# Group 5 Assignment 3 Voters Roll Inspection system

This system is for inspection on the voters roll to checkn whether the details in the system are correct or not.



## Acknowledgements

 - [Whatmore Musarurwa - R145052F](#)
 - [Chamunorwa Nziradzemhuka - R223169H](#)
 - [Andrew Daka - R222726Y](#)
 - [Blessing Chitiyo - R208837A](#)
 - [Cliford Marambire - R102101E](#)
 - [Robert Maneswa - R222261R](#)
 - [Tendai Nyambo - R0537253](#)
 - [Pauline Chikamba - R224987Y](#)
 - [Kudzai Panganai - R0724567P](#)
 - [Munyaradzi Mukuwapasi - R135761F](#)
 - [Clifford Mutava - R224824Z](#)


## Commands

The following commands where used.

```bash
  git init .
  
  git remote add origin https://github.com/whatiecharlton/group5-assignment3-voters-roll-inspection.git
  
  git add .
  
  git commit -m "First Commit"
  
  git push 
```
On the target Server with docker

```bash
  git pull https://github.com/whatiecharlton/group5-assignment3-voters-roll-inspection.git

  docker build -t dockerhub.com/votersroll

  docker tag 0b0b78d4e5ed dockerhub.com/votersroll:latest

  docker push dockerhub.com/votersroll
  
  docker run -p 8080:8080 --name votersroll -d dockerhub.com/votersroll
```
