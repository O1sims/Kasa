System.register(["@angular/http", "../environment/environment", "@angular/core", "rxjs/add/operator/map"], function (exports_1, context_1) {
    "use strict";
    var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
        var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
        if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
        else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
        return c > 3 && r && Object.defineProperty(target, key, r), r;
    };
    var __metadata = (this && this.__metadata) || function (k, v) {
        if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
    };
    var __moduleName = context_1 && context_1.id;
    var http_1, environment_1, core_1, SearchService;
    return {
        setters: [
            function (http_1_1) {
                http_1 = http_1_1;
            },
            function (environment_1_1) {
                environment_1 = environment_1_1;
            },
            function (core_1_1) {
                core_1 = core_1_1;
            },
            function (_1) {
            }
        ],
        execute: function () {
            SearchService = class SearchService {
                constructor(http) {
                    this.http = http;
                    this.api = environment_1.environment.API_HOST + ":" +
                        environment_1.environment.API_PORT + "/api/v" +
                        environment_1.environment.API_VERSION;
                }
                ;
                searchProperties(propertyType, searchQuery) {
                    let params = new http_1.URLSearchParams();
                    params.set('q', searchQuery);
                    var requestoptions = new http_1.RequestOptions({
                        method: http_1.RequestMethod.Get,
                        url: this.api + '/properties/' + propertyType + '/',
                        params: params
                    });
                    return this.http.request(new http_1.Request(requestoptions))
                        .map(res => res.json());
                }
                ;
            };
            SearchService = __decorate([
                core_1.Injectable(),
                __metadata("design:paramtypes", [http_1.Http])
            ], SearchService);
            exports_1("SearchService", SearchService);
            ;
        }
    };
});
