# ------------ co routine ------------

import time

def get_weather_report():
    try:
        print("Please get me lattitude and longitude as tuple")
        geo_str = yield
        print(f"I recieved the data as a tuple: please verify : {geo_str}")
        print("Please get me the parameters to extract")
        geo_par = yield
        print(f"Parameter request is : {geo_par}")
        print("result format expected ")
        result_format = yield
        print(f"Job is done and result is ready in {result_format}")
        final_res = yield
    except GeneratorExit:
        print("Generator stoped from outside")

print("------------ Co routine ------------")
gen1 = get_weather_report()
next(gen1)
gen1.send((1234.567,34566.4433))
time.sleep(3)
gen1.send(("Wind Speed","Humidity"))
time.sleep(3)
gen1.send(("xml","json"))
gen1.close()    #.close() explicitly forces the coroutine to stop executing from the outside.   Why it's used: Because coroutines often sit paused at a yield statement waiting indefinitely for the next .send() call, they can linger in memory and cause resource leaks if left abandoned. Calling .close() injects the GeneratorExit exception into the coroutine, breaks any open loops, and frees up the memory occupied by the generator object.