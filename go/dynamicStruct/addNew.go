package main

import (
	"fmt"

	"github.com/goldeneggg/structil/dynamicstruct/decoder"
)

func main() {
	unknownJSON := []byte(`
{
	"string_field":"かきくけこ",
	"int_field":45678,
	"bool_field":false,
	"object_field":{
		"id":12,
		"name":"the name",
		"nested_object_field": {
			"address": "Tokyo",
			"is_manager": true
		}
	},
	"array_string_field":[
		"array_str_1",
		"array_str_2"
	],
	"array_struct_field":[
		{
			"kkk":"kkk1",
			"vvvv":"vvv1"
		},
		{
			"kkk":"kkk2",
			"vvvv":"vvv2"
		}
	],
	"null_field":null
}
`)

  // create `Decoder` from JSON
  dec, err := decoder.FromJSON(unknownJSON)
  if err != nil {
    panic(err)
  }

  // - If `nest` is true, nested object attributes will be also decoded to struct recursively
  // - If `nest` is false, nested object attributes will be decoded to `map[string]interface{}`
  nest := true

  // - If `useTag` is true, JSON Struct tags are defined
  useTag := true

  // create `DynamicStruct` from `Decoder`
  ds, err := dec.DynamicStruct(nest, useTag)
  if err != nil {
    panic(err)
  }

  // print struct definition from `DynamicStruct`
  fmt.Println(ds.Definition())
}