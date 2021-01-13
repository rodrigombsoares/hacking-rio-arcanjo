import { Component } from '@angular/core';
import { SortingService } from './sorting.service';

@Component({
  selector: 'sorting',
  templateUrl: './sorting.component.html',
  styleUrls: ['./sorting.component.css']
})
export class Sorting {
  title = 'sorting';
  items = []

  constructor(private dataService: SortingService) { }
  
  ngOnInit() {
    this.dataService.sendGetRequest().subscribe((data: any[])=>{
      this.items = data;
    })
  }  
}
