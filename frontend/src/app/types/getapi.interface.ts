interface urls {
  id: number;
  code: string;
  url: string;
  createdAt: Date;
  clicks: number;
}

interface urlsDTO  {
    id: number
    short_url: string
    original_url: string
    clicks: number
    creation_date: string
  }

interface rawRes{
  new_insert:number
}
