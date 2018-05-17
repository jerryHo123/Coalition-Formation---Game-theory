from math import factorial
from itertools import permutations
from itertools import combinations
import itertools as it
#Finding the combinations
def combination(agent_list):
	return [c for i in range(1,len(agent_list)) for c in combinations(agent_list,i)]
#Shapley value calculation for one player at a time
def shapley(current_player):
	temp=0
	temp_array=[]
	for i in range(0,n):
		temp_array.append(0)
	for x in permute:
		current_list=x
		set_s=0
		total_res=0
		#print(current_list)
		for y in range(0,n):
			temp_res=int(res[int(current_list[y])-1])
			if int(current_player)==int(current_list[y]):
				if (total_res*1.0/sum_resource*1.0)*100*1.0<51:
					if(((total_res+temp_res)*1.0/sum_resource*1.0)*100*1.0)>50:
						temp=factorial(set_s)*factorial(n-set_s-1)*10000
						temp_array[y]=temp_array[y]+temp
				
			else:
				set_s = set_s+1
				total_res = total_res+temp_res
	for i in range(0,n):
		 temp_array[i]=int(temp_array[i]/(factorial(i)*factorial(n-i-1)))
	result=0
	result=sum(temp_array)/fact
	return result
#calculating the maximum pay-off an agent can get from a sub-coalition
def max_sub_coalition(current_player_subcoalition):
	result=0
	for x in combination_agent:
		current_list=x
		set_s=0
		total_res=0
		temp_length=len(list(x))
		temp=0
		flag=0
		for i in range(0,temp_length):
			if int(current_player_subcoalition)==int(current_list[i]):
				flag=1
		if flag==1:
			for y in range(0,temp_length):
				temp_res=int(res[int(current_list[y])-1])
				if int(current_player_subcoalition)==int(current_list[y]):
					if (total_res*1.0/sum_resource*1.0)*100*1.0<51:
						if(((total_res+temp_res)*1.0/sum_resource*1.0)*100*1.0)>50 or current_player_subcoalition<=n-3 or n<=3 :
							temp=temp+(factorial(set_s)*factorial(temp_length-set_s-1)*10000)				
				else:
					set_s = set_s+1
					total_res = total_res+temp_res
				temp_result=temp/factorial(temp_length)
				if temp_result>result:
					result=temp_result
	if current_player_subcoalition<=n-3:
		return result/(n-2)
	elif n<=3:	
		return result/2
	else:
		return result
#Getting number of agents from the user
print("\n")
n = int(input("Enter the number of agents : "))
#Factorial Calculation: 
fact=factorial(n)
res=[]
x=1
#Resource for each agent as given by the user
for i in range(1 ,n+1):
	res.append(input("Resource of agent %d : " % x))
	x=x+1
#declaration and definition of the variables being used
agent_list=[]
current_list=[]
result_list=[]
total_res=0
set_s=0
agent=1
sum_resource=0
sub_coalition_result=[]
#Adding up all the resources (total resources)
for i in range (len(res)):
	sum_resource=sum_resource+int(res[i]) 
#Number of agents in a list
for j in range(1,n+1):
	agent_list.append(agent)
	agent=agent+1
#different permutations of the list of agents
permute=list(permutations(range(1,n+1)))
#print(permute)
shapley_result=[]
#Calculating payoff according to shapley values for each agent
#Calling the shapley function
for num in range(0,n):
	current_player=agent_list[num]
	shapley_result.append(shapley(current_player))
	#print(" The utility of Agent ",num+1," is ",result)
print("\n")
print("Shapley Pay-off of all the agents in order : ",shapley_result)
len_combi=len(agent_list)
#Different subcoalitions that can be formed
combination_agent=combination(agent_list)
#print(combination_agent)
#maximum payoff of each agent by forming a subcoalition
for w in range(0,n):
	current_player_subcoalition=agent_list[w]
	sub_coalition_result.append(max_sub_coalition(current_player_subcoalition))
print("Maximum payoff each agent can make by forming a sub-coalition : ",sub_coalition_result)
#Incentive calculation
bribe=0
for i in range(0,n):
	if sub_coalition_result[i]-shapley_result[i]>0:
		temp_difference=sub_coalition_result[i]-shapley_result[i]
		if bribe==0:
			bribe=temp_difference
			bribed_agent=i+1
		if temp_difference<bribe:
			bribe=temp_difference
			bribed_agent=i+1
highest_marginal_contribution=shapley_result.index(max(shapley_result))+1
#print("\n")
#print("Agent ",highest_marginal_contribution," has the highest marginal contribution in a grand coalition based on fairness and has to bribe agent ",bribed_agent," with a payoff of ",bribe)
print("The minimum amount of incentive or the least amount of bribe required for a grand coalition is ",bribe)