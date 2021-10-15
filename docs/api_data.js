define({ "api": [
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
  }
] });
