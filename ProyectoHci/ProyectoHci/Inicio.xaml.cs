using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

using Xamarin.Forms;
using Xamarin.Forms.Xaml;

namespace ProyectoHci
{
    [XamlCompilation(XamlCompilationOptions.Compile)]
    public partial class Inicio : ContentPage
    {
        public Inicio()
        {
            InitializeComponent();
        }

         private async void RegistroPagina(object sender, EventArgs e)
        {
            await Navigation.PushModalAsync(new Registro());
        }

        private async void PeliculasPagina(object sender, EventArgs e)
        {
            await Navigation.PushModalAsync(new Peliculas());
        }
    }
}