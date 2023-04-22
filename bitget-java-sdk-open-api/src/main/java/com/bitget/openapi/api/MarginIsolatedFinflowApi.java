/*
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


package com.bitget.openapi.api;

import com.bitget.openapi.ApiCallback;
import com.bitget.openapi.ApiClient;
import com.bitget.openapi.ApiException;
import com.bitget.openapi.ApiResponse;
import com.bitget.openapi.Configuration;
import com.bitget.openapi.Pair;
import com.bitget.openapi.ProgressRequestBody;
import com.bitget.openapi.ProgressResponseBody;

import com.google.gson.reflect.TypeToken;

import java.io.IOException;


import com.bitget.openapi.model.ApiResponseResultOfMarginIsolatedFinFlowResult;
import com.bitget.openapi.model.ApiResponseResultOfVoid;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import javax.ws.rs.core.GenericType;

public class MarginIsolatedFinflowApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public MarginIsolatedFinflowApi() {
        this(Configuration.getDefaultApiClient());
    }

    public MarginIsolatedFinflowApi(ApiClient apiClient) {
        this.localVarApiClient = apiClient;
    }

    public ApiClient getApiClient() {
        return localVarApiClient;
    }

    public void setApiClient(ApiClient apiClient) {
        this.localVarApiClient = apiClient;
    }

    public int getHostIndex() {
        return localHostIndex;
    }

    public void setHostIndex(int hostIndex) {
        this.localHostIndex = hostIndex;
    }

    public String getCustomBaseUrl() {
        return localCustomBaseUrl;
    }

    public void setCustomBaseUrl(String customBaseUrl) {
        this.localCustomBaseUrl = customBaseUrl;
    }

    /**
     * Build call for isolatedFinList
     * @param symbol symbol (required)
     * @param startTime startTime (required)
     * @param coin coin (optional)
     * @param marginType marginType (optional)
     * @param endTime endTime (optional)
     * @param loanId loanId (optional)
     * @param pageSize pageSize (optional)
     * @param pageId pageId (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 429 </td><td> Gateway Frequency Limit </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Server Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call isolatedFinListCall(String symbol, String startTime, String coin, String marginType, String endTime, String loanId, String pageSize, String pageId, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = null;

        // create path and map variables
        String localVarPath = "/api/margin/v1/isolated/fin/list";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (symbol != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("symbol", symbol));
        }

        if (coin != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("coin", coin));
        }

        if (marginType != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("marginType", marginType));
        }

        if (startTime != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("startTime", startTime));
        }

        if (endTime != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("endTime", endTime));
        }

        if (loanId != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("loanId", loanId));
        }

        if (pageSize != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("pageSize", pageSize));
        }

        if (pageId != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("pageId", pageId));
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "ACCESS_KEY", "ACCESS_PASSPHRASE", "ACCESS_SIGN", "ACCESS_TIMESTAMP", "SECRET_KEY" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call isolatedFinListValidateBeforeCall(String symbol, String startTime, String coin, String marginType, String endTime, String loanId, String pageSize, String pageId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'symbol' is set
        if (symbol == null) {
            throw new ApiException("Missing the required parameter 'symbol' when calling isolatedFinList(Async)");
        }

        // verify the required parameter 'startTime' is set
        if (startTime == null) {
            throw new ApiException("Missing the required parameter 'startTime' when calling isolatedFinList(Async)");
        }

        return isolatedFinListCall(symbol, startTime, coin, marginType, endTime, loanId, pageSize, pageId, _callback);

    }

    /**
     * list
     * Get finance flow List
     * @param symbol symbol (required)
     * @param startTime startTime (required)
     * @param coin coin (optional)
     * @param marginType marginType (optional)
     * @param endTime endTime (optional)
     * @param loanId loanId (optional)
     * @param pageSize pageSize (optional)
     * @param pageId pageId (optional)
     * @return ApiResponseResultOfMarginIsolatedFinFlowResult
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 429 </td><td> Gateway Frequency Limit </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Server Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponseResultOfMarginIsolatedFinFlowResult isolatedFinList(String symbol, String startTime, String coin, String marginType, String endTime, String loanId, String pageSize, String pageId) throws ApiException {
        ApiResponse<ApiResponseResultOfMarginIsolatedFinFlowResult> localVarResp = isolatedFinListWithHttpInfo(symbol, startTime, coin, marginType, endTime, loanId, pageSize, pageId);
        return localVarResp.getData();
    }

    /**
     * list
     * Get finance flow List
     * @param symbol symbol (required)
     * @param startTime startTime (required)
     * @param coin coin (optional)
     * @param marginType marginType (optional)
     * @param endTime endTime (optional)
     * @param loanId loanId (optional)
     * @param pageSize pageSize (optional)
     * @param pageId pageId (optional)
     * @return ApiResponse&lt;ApiResponseResultOfMarginIsolatedFinFlowResult&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 429 </td><td> Gateway Frequency Limit </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Server Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ApiResponseResultOfMarginIsolatedFinFlowResult> isolatedFinListWithHttpInfo(String symbol, String startTime, String coin, String marginType, String endTime, String loanId, String pageSize, String pageId) throws ApiException {
        okhttp3.Call localVarCall = isolatedFinListValidateBeforeCall(symbol, startTime, coin, marginType, endTime, loanId, pageSize, pageId, null);
        Type localVarReturnType = new TypeToken<ApiResponseResultOfMarginIsolatedFinFlowResult>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * list (asynchronously)
     * Get finance flow List
     * @param symbol symbol (required)
     * @param startTime startTime (required)
     * @param coin coin (optional)
     * @param marginType marginType (optional)
     * @param endTime endTime (optional)
     * @param loanId loanId (optional)
     * @param pageSize pageSize (optional)
     * @param pageId pageId (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 429 </td><td> Gateway Frequency Limit </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Server Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call isolatedFinListAsync(String symbol, String startTime, String coin, String marginType, String endTime, String loanId, String pageSize, String pageId, final ApiCallback<ApiResponseResultOfMarginIsolatedFinFlowResult> _callback) throws ApiException {

        okhttp3.Call localVarCall = isolatedFinListValidateBeforeCall(symbol, startTime, coin, marginType, endTime, loanId, pageSize, pageId, _callback);
        Type localVarReturnType = new TypeToken<ApiResponseResultOfMarginIsolatedFinFlowResult>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
