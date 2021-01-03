load("/code_generator/sktools", "protoc")

protoc(
    name = "mmpayauthoritypo_pb_h",
    srcs = [
        "mmpayauthoritypo.proto",
    ],
    outs = [
        "mmpayauthoritypo.pb.cc",
        "mmpayauthoritypo.pb.h",
    ],
)

cc_library(
    name = "mmpayauthoritypo_proto",
    srcs = [
        "mmpayauthoritypo.pb.cc"
    ],
    hdrs = [
        "mmpayauthoritypo.pb.h",
    ],
    includes = ["."],
    deps = [
        "//comm2/svrkit:svrkit_pb",
        
    ],
    copts = [
        '-Wall',
        '-Werror',
    ],
    visibility = ["//visibility:public"],
)

cc_library(
    name = "mmpayauthoritypo",
    deps = [
        ":mmpayauthoritypo_proto"
    ],
    visibility = ["//visibility:public"],
)



protoc(
    name = "mmpayauthoritysimpledo_pb_h",
    srcs = [
        "mmpayauthoritysimpledo.proto",
    ],
    outs = [
        "mmpayauthoritysimpledo.pb.cc",
        "mmpayauthoritysimpledo.pb.h",
    ],
)

cc_library(
    name = "mmpayauthoritysimpledo_proto",
    srcs = [
        "mmpayauthoritysimpledo.pb.cc"
    ],
    hdrs = [
        "mmpayauthoritysimpledo.pb.h",
    ],
    includes = ["."],
    deps = [
        "//comm2/svrkit:svrkit_pb",
        
    ],
    copts = [
        '-Wall',
        '-Werror',
    ],
    visibility = ["//visibility:public"],
)

cc_library(
    name = "mmpayauthoritysimpledo",
    deps = [
        ":mmpayauthoritysimpledo_proto"
    ],
    visibility = ["//visibility:public"],
)



protoc(
    name = "mmpayconfigurationao_pb_h",
    srcs = [
        "mmpayconfigurationao.proto",
    ],
    outs = [
        "mmpayconfigurationao.pb.cc",
        "mmpayconfigurationao.pb.h",
    ],
)

cc_library(
    name = "mmpayconfigurationao_proto",
    srcs = [
        "mmpayconfigurationao.pb.cc"
    ],
    hdrs = [
        "mmpayconfigurationao.pb.h",
    ],
    includes = ["."],
    deps = [
        "//comm2/svrkit:svrkit_pb",
        '//mmpaygitgateway/mmpay_comm/service_export_gen/wxpay/mch_pay_permission/comm/proto:mmpayconfigurationpo_proto'
    ],
    copts = [
        '-Wall',
        '-Werror',
    ],
    visibility = ["//visibility:public"],
)

cc_library(
    name = "mmpayconfigurationao",
    deps = [
        ":mmpayconfigurationao_proto"
    ],
    visibility = ["//visibility:public"],
)



protoc(
    name = "mmpayconfigurationddo_pb_h",
    srcs = [
        "mmpayconfigurationddo.proto",
    ],
    outs = [
        "mmpayconfigurationddo.pb.cc",
        "mmpayconfigurationddo.pb.h",
    ],
)

cc_library(
    name = "mmpayconfigurationddo_proto",
    srcs = [
        "mmpayconfigurationddo.pb.cc"
    ],
    hdrs = [
        "mmpayconfigurationddo.pb.h",
    ],
    includes = ["."],
    deps = [
        "//comm2/svrkit:svrkit_pb",
        
    ],
    copts = [
        '-Wall',
        '-Werror',
    ],
    visibility = ["//visibility:public"],
)

cc_library(
    name = "mmpayconfigurationddo",
    deps = [
        ":mmpayconfigurationddo_proto"
    ],
    visibility = ["//visibility:public"],
)



protoc(
    name = "mmpayconfigurationpo_pb_h",
    srcs = [
        "mmpayconfigurationpo.proto",
    ],
    outs = [
        "mmpayconfigurationpo.pb.cc",
        "mmpayconfigurationpo.pb.h",
    ],
)

cc_library(
    name = "mmpayconfigurationpo_proto",
    srcs = [
        "mmpayconfigurationpo.pb.cc"
    ],
    hdrs = [
        "mmpayconfigurationpo.pb.h",
    ],
    includes = ["."],
    deps = [
        "//comm2/svrkit:svrkit_pb",
        '//mmtenpay/mmpaylog:mmpaylog',
'//mmpaygitgateway/mmpay_comm/service_export_gen/wxpay/mch_pay_permission/comm/proto:mmpaywalletauthlib_proto'
    ],
    copts = [
        '-Wall',
        '-Werror',
    ],
    visibility = ["//visibility:public"],
)

cc_library(
    name = "mmpayconfigurationpo",
    deps = [
        ":mmpayconfigurationpo_proto"
    ],
    visibility = ["//visibility:public"],
)



protoc(
    name = "mmpaydeductauthpo_pb_h",
    srcs = [
        "mmpaydeductauthpo.proto",
    ],
    outs = [
        "mmpaydeductauthpo.pb.cc",
        "mmpaydeductauthpo.pb.h",
    ],
)

cc_library(
    name = "mmpaydeductauthpo_proto",
    srcs = [
        "mmpaydeductauthpo.pb.cc"
    ],
    hdrs = [
        "mmpaydeductauthpo.pb.h",
    ],
    includes = ["."],
    deps = [
        "//comm2/svrkit:svrkit_pb",
        
    ],
    copts = [
        '-Wall',
        '-Werror',
    ],
    visibility = ["//visibility:public"],
)

cc_library(
    name = "mmpaydeductauthpo",
    deps = [
        ":mmpaydeductauthpo_proto"
    ],
    visibility = ["//visibility:public"],
)



protoc(
    name = "mmpaywalletauthlib_pb_h",
    srcs = [
        "mmpaywalletauthlib.proto",
    ],
    outs = [
        "mmpaywalletauthlib.pb.cc",
        "mmpaywalletauthlib.pb.h",
    ],
)

cc_library(
    name = "mmpaywalletauthlib_proto",
    srcs = [
        "mmpaywalletauthlib.pb.cc"
    ],
    hdrs = [
        "mmpaywalletauthlib.pb.h",
    ],
    includes = ["."],
    deps = [
        "//comm2/svrkit:svrkit_pb",
        
    ],
    copts = [
        '-Wall',
        '-Werror',
    ],
    visibility = ["//visibility:public"],
)

cc_library(
    name = "mmpaywalletauthlib",
    deps = [
        ":mmpaywalletauthlib_proto"
    ],
    visibility = ["//visibility:public"],
)
