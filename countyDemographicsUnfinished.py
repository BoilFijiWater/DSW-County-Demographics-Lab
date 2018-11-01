import json
import operator

def main():
    with open('county_demographics.json') as demographics_data:
        counties = json.load(demographics_data)
    print(alphabetically_first_county(counties))
    print(county_most_under_18(counties))
    print(percent_most_under_18(counties))
    print(most_under_18(counties))
    print(state_with_most_counties(counties))

def alphabetically_first_county(counties):
    """Return the county with the name that comes first alphabetically."""
    first = counties[0]["County"]
    for county in counties:
        if county["County"] < first:
            first=county["County"]
    return first

def county_most_under_18(counties):
    """Return the name and state of a county ("<county name>, <state>") with the highest percent of under 18 year olds."""
    first = counties[0]["Age"]["Percent Under 18 Years"]
    name = counties[0]["County"]
    for county in counties:
       if county["Age"]["Percent Under 18 Years"] > first:
           first = county["Age"]["Percent Under 18 Years"]
           name = county["County"]
           state = county["State"]  
    return name + " " + state
  
def percent_most_under_18(counties):
    """Return the highest percent of under 18 year olds."""
    first = counties[0]["Age"]["Percent Under 18 Years"]
    name = counties[0]["County"]
    for county in counties:
       if county["Age"]["Percent Under 18 Years"] > first:
           first = county["Age"]["Percent Under 18 Years"]
           name = county["County"]           
    return first
    
    
def most_under_18(counties):
    """Return a list with the name and state of a county ("<county name>, <state>") and the percent of under 18 year olds for a county with the highest percent of under 18 year olds."""
    first = counties[0]["Age"]["Percent Under 18 Years"]
    name = counties[0]["County"]
    for county in counties:
       if county["Age"]["Percent Under 18 Years"] > first:
           first = county["Age"]["Percent Under 18 Years"]
           name = county["County"]           
    return county_most_under_18(counties) + " " + str(first) 
    
def state_with_most_counties(counties):
    """Return a state that has the most counties."""
    #Make a dictionary that has a key for each state and the values keep track of the number of counties in each state   
    #Find the state in the dictionary with the most counties 
    #Return the state with the most counties
     
    states = {} 
    
    for c in counties:
        cc = c["State"]
        if cc in states:
            states[cc] += 1
        else:
            states[cc] = 1
    
    states = sorted(states.items(), key=operator.states(1))
    return states 
        
        
    
    
    
def your_interesting_demographic_function(counties):
    """Compute and return an interesting fact using the demographic data about the counties in the US."""

if __name__ == '__main__':
    main()
