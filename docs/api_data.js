define({ "api": [
  {
    "type": "POST",
    "url": "/login",
    "title": "Login and recieve token",
    "name": "Login",
    "group": "Authentication",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "username",
            "description": "<p>Username</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "password",
            "description": "<p>Password</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "{",
          "content": "{\n    \"username\": \"joe\",\n    \"password\": \"shep\",\n}",
          "type": "json"
        }
      ]
    },
    "success": {
      "fields": {
        "200": [
          {
            "group": "200",
            "type": "Object",
            "optional": false,
            "field": "credentials",
            "description": "<p>Logged in user's credentials</p>"
          },
          {
            "group": "200",
            "type": "credentials.token",
            "optional": false,
            "field": "Logged",
            "description": "<p>in user's authorization token</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "(200) {json}",
          "content": "{\n    \"token\": \"9ba45f09651c5b0c404f37a2d2572c026c146694\"\n}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "rgblent_api/views/auth.py",
    "groupTitle": "Authentication"
  },
  {
    "type": "POST",
    "url": "/register",
    "title": "Register and recieve token",
    "name": "Register",
    "group": "Authentication",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "username",
            "description": "<p>Username</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "password",
            "description": "<p>Password</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "first_name",
            "description": "<p>First name</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "last_name",
            "description": "<p>Last name</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "email",
            "description": "<p>Email</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "{",
          "content": "{\n    \"first_name\": \"Joe\",\n    \"last_name\": \"Shepherd\",\n    \"email\": \"joe@joeshepherd.com\",\n    \"username\": \"joe\",\n    \"password\": \"shep\",\n}",
          "type": "json"
        }
      ]
    },
    "success": {
      "fields": {
        "200": [
          {
            "group": "200",
            "type": "Object",
            "optional": false,
            "field": "credentials",
            "description": "<p>Registered user's credentials</p>"
          },
          {
            "group": "200",
            "type": "credentials.",
            "optional": false,
            "field": "credentials.token",
            "description": "<p>Registered user's authorization token</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "(200) {json}",
          "content": "{\n    \"token\": \"9ba45f09651c5b0c404f37a2d2572c026c146694\"\n}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "rgblent_api/views/auth.py",
    "groupTitle": "Authentication"
  },
  {
    "type": "POST",
    "url": "/colorblend",
    "title": "POST two colors and get the result of blending them together",
    "name": "Blend",
    "group": "Color",
    "version": "0.0.0",
    "filename": "rgblent_api/views/color.py",
    "groupTitle": "Color"
  },
  {
    "type": "POST",
    "url": "/colorinfo",
    "title": "POST get detailed information on a color",
    "name": "Info",
    "group": "Color",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "rgb_hex",
            "description": "<p>The provided color as a hex string</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "{",
          "content": "{\n    \"rgb_hex\": \"#405060\"\n}",
          "type": "json"
        }
      ]
    },
    "success": {
      "fields": {
        "200": [
          {
            "group": "200",
            "type": "Object",
            "optional": false,
            "field": "color_info",
            "description": "<p>The provided color translated to different colorspaces</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "(200) {json}",
          "content": "{\n    \"rgb\": {\n        \"rgb_r\": 64.0,\n        \"rgb_g\": 80.0,\n        \"rgb_b\": 96.0,\n        \"is_upscaled\": false,\n    },\n    \"hsl\": {\n        \"hsl_h\": 210.0,\n        \"hsl_s\": -0.202531645556962025,\n        \"hsl_l\": 80.0\n    },\n    \"hsv\": {\n        \"hsv_h\": 210.0,\n        \"hsv_s\": 0.3333333333337,\n        \"hsv_v\": 96.0\n    },\n    \"lab\": {\n        \"lab_l\": 3636.209104440874,\n        \"lab_a\": -150.7336722215644,\n        \"lab_b\": -982.4912665013201,\n        \"observer\": \"2\",\n        \"illuminant\": \"d65\",\n    },\n    \"xyz\": {\n        \"xyz_x\": 28581.772648563052,\n        \"xyz_y\": 30954.276615825478,\n        \"xyz_z\": 52127.62204019337,\n        \"observer\": \"2\",\n        \"illuminant\": \"d65\",\n    }\n}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "rgblent_api/views/color.py",
    "groupTitle": "Color"
  },
  {
    "type": "GET",
    "url": "/default/palette",
    "title": "GET default palette",
    "name": "DefaultPalette",
    "group": "Palette",
    "success": {
      "fields": {
        "200": [
          {
            "group": "200",
            "type": "Object",
            "optional": false,
            "field": "palette",
            "description": "<p>Retrieved default palette</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success",
          "content": "[\n      {\n           \"rgb_hex\" => \"#FFDF80\",\n               \"red\" => 255,\n             \"green\" => 223,\n              \"blue\" => 128,\n           \"builtin\" => false,\n        \"is_default\" => true\n      },\n      {\n           \"rgb_hex\" => \"#BFFF80\",\n               \"red\" => 191,\n             \"green\" => 255,\n              \"blue\" => 128,\n           \"builtin\" => false,\n        \"is_default\" => true\n      },\n      {\n           \"rgb_hex\" => \"#80FF9F\",\n               \"red\" => 128,\n             \"green\" => 255,\n              \"blue\" => 159,\n           \"builtin\" => false,\n        \"is_default\" => true\n      },\n      {\n           \"rgb_hex\" => \"#80FFFF\",\n               \"red\" => 128,\n             \"green\" => 255,\n              \"blue\" => 255,\n           \"builtin\" => false,\n        \"is_default\" => true\n      },\n      {\n           \"rgb_hex\" => \"#809FFF\",\n               \"red\" => 128,\n             \"green\" => 159,\n              \"blue\" => 255,\n           \"builtin\" => false,\n        \"is_default\" => true\n      },\n      {\n           \"rgb_hex\" => \"#BF80FF\",\n               \"red\" => 191,\n             \"green\" => 128,\n              \"blue\" => 255,\n           \"builtin\" => false,\n        \"is_default\" => true\n      },\n      {\n           \"rgb_hex\" => \"#FF80DF\",\n               \"red\" => 255,\n             \"green\" => 128,\n              \"blue\" => 223,\n           \"builtin\" => false,\n        \"is_default\" => true\n      },\n      {\n           \"rgb_hex\" => \"#FF8080\",\n               \"red\" => 255,\n             \"green\" => 128,\n              \"blue\" => 128,\n           \"builtin\" => false,\n        \"is_default\" => true\n      }\n]",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "rgblent_api/views/palette.py",
    "groupTitle": "Palette"
  },
  {
    "type": "POST",
    "url": "/profile/favorite",
    "title": "POST new favorite",
    "name": "CreateFavorite",
    "group": "Profile",
    "success": {
      "fields": {
        "200": [
          {
            "group": "200",
            "type": "Object",
            "optional": false,
            "field": "user_color",
            "description": "<p>The newly created UserColor object</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "{",
          "content": "{\n      \"id\" => 168,\n   \"label\" => \"my_fave\",\n   \"color\" => {\n            \"id\" => 174,\n       \"rgb_hex\" => \"#012345\",\n           \"red\" => 1,\n         \"green\" => 35,\n          \"blue\" => 69,\n       \"builtin\" => false,\n    \"is_default\" => false\n  },\n  \"isMine\" => true\n}",
          "type": "Object"
        }
      ]
    },
    "error": {
      "fields": {
        "409 CONFLICT -- Already Exists": [
          {
            "group": "409 CONFLICT -- Already Exists",
            "type": "Object",
            "optional": false,
            "field": "user_color",
            "description": "<p>The already created UserColor object</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "{",
          "content": "{\n      \"id\" => 168,\n   \"label\" => \"my_fave\",\n   \"color\" => {\n            \"id\" => 174,\n       \"rgb_hex\" => \"#012345\",\n           \"red\" => 1,\n         \"green\" => 35,\n          \"blue\" => 69,\n       \"builtin\" => false,\n    \"is_default\" => false\n  },\n  \"isMine\" => true\n}",
          "type": "Object"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "rgblent_api/views/user.py",
    "groupTitle": "Profile",
    "header": {
      "fields": {
        "Header": [
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "Authorization",
            "description": "<p>Auth token</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Authorization ",
          "content": "Token 9ba45f09651c5b0c404f37a2d2572c026c146694",
          "type": "String"
        }
      ]
    }
  },
  {
    "type": "GET",
    "url": "/profile",
    "title": "GET the current user's profile",
    "name": "GetProfile",
    "group": "Profile",
    "success": {
      "fields": {
        "200": [
          {
            "group": "200",
            "type": "Object",
            "optional": false,
            "field": "user",
            "description": "<p>Current user's profile</p>"
          },
          {
            "group": "200",
            "type": "id",
            "optional": false,
            "field": "user.id",
            "description": "<p>Current user's id</p>"
          },
          {
            "group": "200",
            "type": "String",
            "optional": false,
            "field": "user.name",
            "description": "<p>Current user's name</p>"
          },
          {
            "group": "200",
            "type": "String",
            "optional": false,
            "field": "user.username",
            "description": "<p>Current user's username</p>"
          },
          {
            "group": "200",
            "type": "String",
            "optional": false,
            "field": "user.email",
            "description": "<p>Current user's email</p>"
          },
          {
            "group": "200",
            "type": "Array",
            "optional": false,
            "field": "user.colors",
            "description": "<p>UserColor objects representing the current user's favorited colors</p>"
          },
          {
            "group": "200",
            "type": "Array",
            "optional": false,
            "field": "user.palettes",
            "description": "<p>Palette objects representing the current user's saved palettes</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Input",
          "content": "{\n    \"id\": 1\n    \"name\": \"Joe Shepherd\",\n    \"username\": \"joe\",\n    \"email\": \"joe@joeshepherd.com\"\n    \"colors\": []\n    \"palettes\": []\n}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "rgblent_api/views/user.py",
    "groupTitle": "Profile",
    "header": {
      "fields": {
        "Header": [
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "Authorization",
            "description": "<p>Auth token</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Authorization ",
          "content": "Token 9ba45f09651c5b0c404f37a2d2572c026c146694",
          "type": "String"
        }
      ]
    }
  }
] });
