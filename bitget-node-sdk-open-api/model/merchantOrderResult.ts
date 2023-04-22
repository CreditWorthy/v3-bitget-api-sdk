/**
 * Bitget Open API
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2.0.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

import { RequestFile } from './models';
import { MerchantOrderInfo } from './merchantOrderInfo';

export class MerchantOrderResult {
    'minId'?: string;
    'orderList'?: Array<MerchantOrderInfo>;

    static discriminator: string | undefined = undefined;

    static attributeTypeMap: Array<{name: string, baseName: string, type: string}> = [
        {
            "name": "minId",
            "baseName": "minId",
            "type": "string"
        },
        {
            "name": "orderList",
            "baseName": "orderList",
            "type": "Array<MerchantOrderInfo>"
        }    ];

    static getAttributeTypeMap() {
        return MerchantOrderResult.attributeTypeMap;
    }
}

