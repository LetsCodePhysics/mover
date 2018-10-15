def move(duration,delta_t,args):
    time = 0
    while (time < duration):
      rate(50)
      for obj in args:
        obj.velocity = obj.velocity + obj.force/obj.mass*delta_t
        obj.pos = obj.pos + obj.velocity*delta_t
      time = time + delta_t
    return
