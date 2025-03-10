# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.

# You should have received a copy of the GNU Lesser General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

# Author: Pau Manyer Fuertes
# Email: pau.manyer@bsc.es
# Date: October 2024
# Institution: Barcelona Supercomputing Center (BSC)
# Department: Computer Applications in Science and Engineering (CASE)
# Research Group: Nuclear Fusion  

# This script constitutes the test-suite for the FIXED-boundary plasma equilibrium problem 
# where the plasma current is modelled using a LINEAR function. Such case yields an analytical 
# solution, an therefore the exact numerical error can be computed and used for code validation. 

# After selecting the MESH, the file may be executed to launch the solver. EQUILIPY's output can 
# be turned ON and OFF by change the bolean output parameters.



import sys
sys.path.append('../src')

from GradShafranovCutFEM import *

### SELECT MESH 
#MESH = 'TS-CUTFEM-TRI03-FINE-REDUCED'
MESH = 'TS-CUTFEM-TRI06-MEDIUM-REDUCED'
#MESH = 'TS-CUTFEM-TRI10-LOW-REDUCED'
#MESH = 'TS-CUTFEM-QUA04-FINE-REDUCED'
#MESH = 'TS-CUTFEM-QUA09-FINE-REDUCED'

CASE = 'TS-FIXED-1W-LINEAR'   

##############################################################
##############################################################

## CREATE GRAD-SHAFRANOV PROBLEM 
Problem = GradShafranovCutFEM(MESH,CASE)
## DECLARE OUTPUT SWITCHS:
##### OUTPUT PLOTS IN RUNTIME
Problem.plotElemsClassi_output = False        # OUTPUT SWITCH FOR ELEMENTS CLASSIFICATION PLOTS AT EACH ITERATION
Problem.plotPSI_output = True                 # OUTPUT SWITCH FOR PSI SOLUTION PLOTS AT EACH ITERATION
##### OUTPUT FILES
Problem.PARAMS_output = True                  # OUTPUT SWITCH FOR SIMULATION PARAMETERS 
Problem.PSI_output = True                     # OUTPUT SWITCH FOR PSI FIELD VALUES OBTAINED BY SOLVING THE CutFEM SYSTEM
Problem.PSIcrit_output = False                # OUTPUT SWITCH FOR CRITICAL PSI VALUES
Problem.PSI_NORM_output = False               # OUTPUT SWITCH FOR THE PSI_NORM FIELD VALUES (AFTER NORMALISATION OF PSI FIELD)
Problem.PSI_B_output = False                  # OUTPUT SWITCH FOR PSI_B BOUNDARY VALUES
Problem.RESIDU_output = True                  # OUTPUT SWITCH FOR RESIDU FOR EACH ITERATION
Problem.ElementsClassi_output = False         # OUTPUT SWITCH FOR CLASSIFICATION OF MESH ELEMENTS
Problem.PlasmaLevSetVals_output = False       # OUTPUT SWITCH FOR PLASMA BOUNDARY LEVEL-SET FIELD VALUES
Problem.VacVessLevSetVals_output = False      # OUTPUT SWITCH FOR VACUUM VESSEL BOUNDARY LEVEL-SET FIELD VALUES
Problem.L2error_output = True                 # OUTPUT SWITCH FOR ERROR FIELD AND THE L2 ERROR NORM FOR THE CONVERGED SOLUTION 
Problem.ELMAT_output = False                  # OUTPUT SWITCH FOR ELEMENTAL MATRICES

##############################################################
##############################################################

## COMPUTE PLASMA EQUILIBRIUM
Problem.EQUILI()