概述

基于redis实现的唯一序列值，原则操作，不会重复。

格式

时间戳+8位自增数值，8位自增数值每天重新置0

例如：

155411573353966200000261

155411573354327300000262

155411573354339900000263

155411573354354800000264

155411573354366500000265

155411573354381100000266

155411573354392200000267

155411573354402200000268

155411573354411700000269

155411573354420900000270