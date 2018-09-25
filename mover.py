def move(duration,delta_t,object, *objects):
    time = 0
    while (time < duration):
        rate(50)
        object.velocity = object.velocity + object.force/object.mass*delta_t
        object.pos = object.pos + object.velocity*delta_t
        for obj in objects:
            obj.velocity = obj.velocity + obj.force/obj.mass*delta_t
            obj.pos = obj.pos + obj.velocity*delta_t
        
        
        time = time + delta_t
    return