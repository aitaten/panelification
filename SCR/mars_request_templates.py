mars_request_templates = {
"ifs-highres" :"""retrieve,
  class = od,
  type = fc,
  stream = {stream},
  expver = 0001,
  levtype = sfc,
  param = 228.128,
  date = {date},
  time = {time},
  step = {step},
  padding = 0,
  expect = any,
  repres = gg,
  area=E,
  grid=F1280,
  database = marsod,
  target = {target}""",
'ifs-dt' : """retrieve,
  class = od,
  dataset = extremes-dt,
  expver = 0001,
  stream = oper,
  type = fc,
  date = {date},
  time = {time},
  step = {step},
  levtype = sfc,
  param = 228.128,
  area  = 75./-10./30./35.,
  target = {target}""",

# 'ifs-dt' : """retrieve,
#   class = rd,
#   dataset = research,
#   expver = i4ql,
#   stream = {stream},
#   type = fc,
#   date = {date},
#   time = {time},
#   step = {step},
#   levtype = sfc,
#   param = 228.128,
#   area = 58./-10./30./25,
#   target = {target}""",
# 'ifs-dt' : """retrieve,
#   class = rd,
#   date = {date},
#   expver = i8hy,
#   levtype = sfc,
#   param = 228.128,
#   step = {step},
#   stream = oper,
#   time = {time},
#   type = fc,
#   area = 58./0./40./25,
#   target = {target}""",
'dt_nc' : """retrieve,
  class = rd,
  date = {date},
  expver = i6ux,
  levtype = sfc,
  param = 228.128,
  step = {step},
  stream = oper,
  time = {time},
  type = fc,
  area = 58./-8./40./25,
  target = {target}"""
}
