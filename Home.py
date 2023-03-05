import streamlit as st

st.set_page_config(page_title="Home",page_icon="🏠",layout="centered")


st.write(st.__version__)

st.write("# iLivery Growth Dashboard")
st.write("###### Growth Dashboard created to track the metrics of the deliverers and restaurants in the marketplace")

st.markdown(
    """
### How to use the dashboard?

You can use the available filters on the sidebar to change the data under analysis (Date, traffic and weather) 

### Understanding the content

#### - Strategy Panorama

• Orders per Day | Show the relation between the amount of orders and a date. 
Here you can identify patterns and trends. This can help identify which days 
have higher or lower order volumes and link them to various factors,
such as the start of the week, weekends, seasons, and holidays. This way 
decision maker can use can this information to develop strategies such as 
offering promotions or discounts on slower days, increasing staffing levels 
during peak times, and optimizing delivery routes to ensure orders are delivered 
efficiently. 


• Quantity of Orders per City and Traffic Density | With this chart, you can 
identify areas with a high order volume and traffic density. This can help determine 
the optimal allocation of resources, including identifying areas where there is high demand 
for food delivery services and giving mobility preference to vehicles that can efficiently 
cover these areas while considering traffic conditions. Moreover, knowing the traffic 
conditions in an area is crucial to anticipating delays and cancellations.
You can also identify areas with low company presence and incentivize restaurants and delivery 
personnel in these areas by offering benefits and incentives, such as higher pay or promotional
offers. This can help increase the company's presence and customer base in the area, improving customer satisfaction


• Orders per Weathercondition | This pie chart relates weathercondition to the demand. Here you can 
identify bad weather days according to the forecast and give preference to restaurants and houses
located within a safe range that can ensure the safety of the delivery personnel and the orders and also
reduce delays and cancellations. 
This may involve reducing the range of delivery and prioritizing mobility options such as cars 
instead of bikes, especially during heavy rain or snowfall. Decision maker can also relate weather
condition to the demand for food delivery services. During bad weather conditions, customers may 
prefer to stay at home and order food, which may result in higher order volumes. Conversely, during 
good weather conditions, customers may prefer to go out and eat at restaurants.

• Orders per Week | Looking at the amount of orders per week is a good way to understand how a marketing
campaign worked and how a change in decision impacted demand or the impact of a promotion/discounts. 
Analyzing the data per week can be more accurate than analyzing per day because you are less vulnerable 
to the fluctuations caused by unusual or random events.


• Average Weekly Orders per Delivery Person | This chart can provide useful information. For example,
you can determine with it and also with the assistance of the orders per week chart which season is best
to stimulate demand with promotions, combos and discounts to increase the workload for the deliverers.
Additionaly, you can identify days when the deliverers are overloaded, which can help you optimeze your
delivery operations, it could also indicate that there is either a shortage of delivery person.

• Deliveries geo center | The map displays the geometric centers of the deliveries. In this hot spot area
you can provide discounts and select the best vehicle for delivery in the area. For example, if the majority
of deliveries concentrate near the restaurants and clients who order the most, and the distance is short, 
you can prioritize bikes or motorcycles. For deliverers far away from the centers, other types of mobility
may be preferred. Close to this center is also the best place to implement supporting points for the deliverers, 
since most of the deliveries are done in this area, you can expect the majority of your delivery personnel to 
pass through this area. Therefore, having spots where they can rest and take a break to have a coffee is a good idea.
This area with the highest concentration of deliveries may be the best places to gather feedback through surveys or
measure the effectiveness of a marketing campaign. These areas have a higher volume, providing a larger sample for
data collection.
                            
#### - Deliverers description
    
• Deliverer Ratings | This table show in descend order the deliverers with highests ratings in your database,
by identifying the highest ratings deliverers and giving them benefits you encourage good practice between your 
delivery personal. It can also help you identify any deliverers with consistently low ratings and provide them 
additional training or reassigning them to different delivery routes. Additionally, you can use this information to
make decisions about which deliverers to prioritize for certain high-value or challenging deliveries.
    
• Deliverer Ratings per Weather Condition/Traffic | Weather conditions, as well as traffic, are important parameters to 
consider when analyzing the ratings of delivery personnel. It is expected that deliverers who frequently drive in 
bad weather conditions/traffic density are more likely to receive low ratings due to delays. On the other hand, 
if a delivery person manages to deliver the food quickly and still hot despite challenging weather conditions/high traffic, 
customers might appreciate their effort and give them higher ratings. It is a good idea to take weather conditions into 
account when analyzing ratings and to be more tolerant of low ratings in these cases.

• Vehicles | Knowing the distribution of the vehicles used by your delivery personnel is important because it allows you
to assess whether the vehicle is appropriate for the type of deliveries being made. For example, bicycles are suitable 
for short-distance deliveries, but may not be appropriate for long distances or hilly areas. By understanding the vehicles 
being used, you can improve efficiency and reduce costs by minimizing delays and cancellations.

• Fastest/Slowest Deliverer | These charts give us a list of deliverers ranked by their average delivery time. Together with
the ratings, they are important parameters for evaluating your delivery personnel. However, it's also crucial to consider 
other factors such as the distance of the delivery, traffic, and weather conditions. It's important to ensure that the deliverers 
listed as the fastest are respecting traffic rules, and for those listed as the slowest, further analysis is needed to identify 
the cause of their low results, such as vehicle type and condition, average distance of the route, weather conditions, and traffic density.
    
#### - Restaurants View

• Time Taken per City and Traffic Density | This chart can help identify areas with high traffic congestion where deliveries 
are taking longer than usual. Depending on the traffic density and city area, certain types of vehicles may be better suited 
for deliveries. For example, scooters or e-scooters may be more efficient in densely populated areas with heavy traffic, 
while motorcycles may be more appropriate for deliveries in suburban or rural areas. This information can also help gain 
a better understanding of how traffic affects delivery times. This information can be used to make more accurate delivery
time estimates, potentially reducing customer frustration and improving satisfaction.

• Type of Order | Identifying how which kind of order is performing can give you information necessary to pricing, promotions
and future menus. Additionally, you can stimulate the demand for type of orders that are perfoming bad.

• Localization of Restaurants | Helpful for optimizing your delivey operations. You can identify areas where there may be a 
higher demand for deliveries, and allocate your delivery personnel accordingly. Additionally, you can identify potential areas 
for expansion or partnership with new restaurants.

#### Ask for Help
Discord Alain Ramon Burkhard #6807
"""
)

st.sidebar.markdown('# iLivery')
st.sidebar.markdown('## Fast Home Food')
st.sidebar.markdown("""---""")
