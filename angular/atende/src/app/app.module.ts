import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { CheckinComponent } from './checkin/checkin.component';
import { Sorting } from './sorting/sorting.component'
import { HttpClientModule } from '@angular/common/http';


@NgModule({
  declarations: [
    Sorting,
    AppComponent,
    CheckinComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
