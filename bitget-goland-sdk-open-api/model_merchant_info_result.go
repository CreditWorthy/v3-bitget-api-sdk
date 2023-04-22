/*
Bitget Open API

No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

API version: 2.0.0
*/

// Code generated by OpenAPI Generator (https://openapi-generator.tech); DO NOT EDIT.

package openapi

import (
	"encoding/json"
)

// MerchantInfoResult struct for MerchantInfoResult
type MerchantInfoResult struct {
	MinId                *string        `json:"minId,omitempty"`
	ResultList           []MerchantInfo `json:"resultList,omitempty"`
	AdditionalProperties map[string]interface{}
}

type _MerchantInfoResult MerchantInfoResult

// NewMerchantInfoResult instantiates a new MerchantInfoResult object
// This constructor will assign default values to properties that have it defined,
// and makes sure properties required by API are set, but the set of arguments
// will change when the set of required properties is changed
func NewMerchantInfoResult() *MerchantInfoResult {
	this := MerchantInfoResult{}
	return &this
}

// NewMerchantInfoResultWithDefaults instantiates a new MerchantInfoResult object
// This constructor will only assign default values to properties that have it defined,
// but it doesn't guarantee that properties required by API are set
func NewMerchantInfoResultWithDefaults() *MerchantInfoResult {
	this := MerchantInfoResult{}
	return &this
}

// GetMinId returns the MinId field value if set, zero value otherwise.
func (o *MerchantInfoResult) GetMinId() string {
	if o == nil || isNil(o.MinId) {
		var ret string
		return ret
	}
	return *o.MinId
}

// GetMinIdOk returns a tuple with the MinId field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *MerchantInfoResult) GetMinIdOk() (*string, bool) {
	if o == nil || isNil(o.MinId) {
		return nil, false
	}
	return o.MinId, true
}

// HasMinId returns a boolean if a field has been set.
func (o *MerchantInfoResult) HasMinId() bool {
	if o != nil && !isNil(o.MinId) {
		return true
	}

	return false
}

// SetMinId gets a reference to the given string and assigns it to the MinId field.
func (o *MerchantInfoResult) SetMinId(v string) {
	o.MinId = &v
}

// GetResultList returns the ResultList field value if set, zero value otherwise.
func (o *MerchantInfoResult) GetResultList() []MerchantInfo {
	if o == nil || isNil(o.ResultList) {
		var ret []MerchantInfo
		return ret
	}
	return o.ResultList
}

// GetResultListOk returns a tuple with the ResultList field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *MerchantInfoResult) GetResultListOk() ([]MerchantInfo, bool) {
	if o == nil || isNil(o.ResultList) {
		return nil, false
	}
	return o.ResultList, true
}

// HasResultList returns a boolean if a field has been set.
func (o *MerchantInfoResult) HasResultList() bool {
	if o != nil && !isNil(o.ResultList) {
		return true
	}

	return false
}

// SetResultList gets a reference to the given []MerchantInfo and assigns it to the ResultList field.
func (o *MerchantInfoResult) SetResultList(v []MerchantInfo) {
	o.ResultList = v
}

func (o MerchantInfoResult) MarshalJSON() ([]byte, error) {
	toSerialize := map[string]interface{}{}
	if !isNil(o.MinId) {
		toSerialize["minId"] = o.MinId
	}
	if !isNil(o.ResultList) {
		toSerialize["resultList"] = o.ResultList
	}

	for key, value := range o.AdditionalProperties {
		toSerialize[key] = value
	}

	return json.Marshal(toSerialize)
}

func (o *MerchantInfoResult) UnmarshalJSON(bytes []byte) (err error) {
	varMerchantInfoResult := _MerchantInfoResult{}

	if err = json.Unmarshal(bytes, &varMerchantInfoResult); err == nil {
		*o = MerchantInfoResult(varMerchantInfoResult)
	}

	additionalProperties := make(map[string]interface{})

	if err = json.Unmarshal(bytes, &additionalProperties); err == nil {
		delete(additionalProperties, "minId")
		delete(additionalProperties, "resultList")
		o.AdditionalProperties = additionalProperties
	}

	return err
}

type NullableMerchantInfoResult struct {
	value *MerchantInfoResult
	isSet bool
}

func (v NullableMerchantInfoResult) Get() *MerchantInfoResult {
	return v.value
}

func (v *NullableMerchantInfoResult) Set(val *MerchantInfoResult) {
	v.value = val
	v.isSet = true
}

func (v NullableMerchantInfoResult) IsSet() bool {
	return v.isSet
}

func (v *NullableMerchantInfoResult) Unset() {
	v.value = nil
	v.isSet = false
}

func NewNullableMerchantInfoResult(val *MerchantInfoResult) *NullableMerchantInfoResult {
	return &NullableMerchantInfoResult{value: val, isSet: true}
}

func (v NullableMerchantInfoResult) MarshalJSON() ([]byte, error) {
	return json.Marshal(v.value)
}

func (v *NullableMerchantInfoResult) UnmarshalJSON(src []byte) error {
	v.isSet = true
	return json.Unmarshal(src, &v.value)
}
