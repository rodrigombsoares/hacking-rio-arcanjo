import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { CheckinComponent } from './checkin/checkin.component';
import { Sorting } from './sorting/sorting.component';


const routes: Routes = [
  { path: 'checkin', component: CheckinComponent },
  { path: 'sorting', component: Sorting }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
